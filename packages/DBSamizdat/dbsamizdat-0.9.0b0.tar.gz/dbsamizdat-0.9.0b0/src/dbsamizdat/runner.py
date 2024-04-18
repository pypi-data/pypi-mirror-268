import argparse
import sys
from time import monotonic
from logging import getLogger
from enum import Enum
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import cpu_count
from typing import Generator
from functools import partial

import psycopg2

from .libdb import dbinfo_to_class, dbstate_equals_definedstate, get_dbstate, DBObjectType
from .libgraph import depsort_with_sidekicks, node_dump, sanity_check, subtree_depends, deps_on_closure
from .graphvizdot import dot
from .loader import get_samizdats
from . import entitypes
from .exceptions import SamizdatException, DatabaseError, FunctionSignatureError, WrongTransactionStyleForParallelRefresh
from .util import fqify_node, nodenamefmt, sqlfmt, honest_cursor


class txstyle(Enum):
    CHECKPOINT = 'checkpoint'
    JUMBO = 'jumbo'
    DRYRUN = 'dryrun'


logger = getLogger(__name__)
PRINTKWARGS = dict(file=sys.stderr, flush=True)
MAX_ACTION_VERB_LENGTH = 14
ENTITYTYPE_LENGTH = 17


def vprint(args: argparse.Namespace, *pargs, **pkwargs):
    if args.log_rather_than_print:
        logger.info(' '.join(map(str, pargs)))
    elif args.verbosity:
        print(*pargs, **{**PRINTKWARGS, **pkwargs})


def vvprint(args: argparse.Namespace, *pargs, **pkwargs):
    if args.log_rather_than_print:
        logger.debug(' '.join(map(str, pargs)))
    elif args.verbosity > 1:
        print(*pargs, **{**PRINTKWARGS, **pkwargs})


def get_executor_drainer(args, max_namelen=0, parallel=False):
    if args.log_rather_than_print:
        return log_drain_executor
    return partial(chronoprint_drain_executor, args, max_namelen=max_namelen, parallel=parallel)


def log_drain_executor(executor: Generator):
    for timing, action_totake, sd, sql in executor:
        what = "STARTING" if timing is None else "FINISHED (%.2fs)" % timing
        logger.info(f"""{what} {action_totake} {sd.entity_type.value} {sd}""")
        logger.debug(f"""Generated SQL for {action_totake} {sd.entity_type.value} {sd}:\n{sqlfmt(sql)}""")


def chronoprint_drain_executor(args, executor: Generator, max_namelen=0, parallel=False):
    if parallel:
        # starts and finishes are interwoven
        for timing, action_totake, sd, sql in executor:
            what = "start " if timing is None else "finish"
            if timing is None:
                vprint(args, f'%-{MAX_ACTION_VERB_LENGTH}s %-{ENTITYTYPE_LENGTH}s %-{max_namelen}s' % (f'{what} {action_totake}', sd.entity_type.value, sd))
                vvprint(args, f'\n\n{sqlfmt(sql)}\n\n')
            else:
                vprint(args, f'%-{MAX_ACTION_VERB_LENGTH}s %-{ENTITYTYPE_LENGTH}s %-{max_namelen}s %7.2fs' % (f'{what} {action_totake}', sd.entity_type.value, sd, timing))
    else:
        # finishes directly follow starts for the same object
        for timing, action_totake, sd, sql in executor:
            if timing:
                vprint(args, '%7.2fs' % timing)
            else:
                vprint(args, f'%-{MAX_ACTION_VERB_LENGTH}s %-{ENTITYTYPE_LENGTH}s %-{max_namelen}s ' % (action_totake, sd.entity_type.value, sd), end='')
                vvprint(args, f'\n\n{sqlfmt(sql)}\n\n')


def get_cursor(args):
    cursor = None
    if args.in_django:
        from django.db import connections
        cursor = honest_cursor(connections[args.dbconn].cursor())
    else:
        cursor = psycopg2.connect(args.dburl).cursor()
    cursor.execute('BEGIN;')  # And so it begins…
    return cursor


def txi_finalize(cursor, args):
    do_what = {txstyle.JUMBO.value: 'COMMIT;', txstyle.DRYRUN.value: 'ROLLBACK;'}.get(args.txdiscipline)
    if do_what:
        cursor.execute(do_what)


def cmd_refresh(args):
    if args.parallel and args.txdiscipline != txstyle.CHECKPOINT.value:
        raise WrongTransactionStyleForParallelRefresh()

    cursor = get_cursor(args)
    samizdats = depsort_with_sidekicks(sanity_check(get_samizdats(args.samizdatmodules)))
    matviews = [sd for sd in samizdats if sd.entity_type == entitypes.MATVIEW]

    if args.belownodes:
        rootnodes = {fqify_node(rootnode) for rootnode in args.belownodes}
        allnodes = node_dump(samizdats)
        if rootnodes - allnodes:
            raise ValueError('''Unknown rootnodes:\n\t- %s''' % '\n\t- '.join([nodenamefmt(rootnode) for rootnode in rootnodes - allnodes]))
        subtree_bundle = subtree_depends(samizdats, rootnodes)
        matviews = [sd for sd in matviews if sd in subtree_bundle]

    max_namelen = max(len(str(ds)) for ds in matviews)

    def refreshes(subjects):
        for sd in subjects:
            yield 'refresh', sd, sd.refresh(concurrent_allowed=True)

    drain = get_executor_drainer(args, max_namelen=max_namelen, parallel=args.parallel)
    if args.parallel:
        firstlevel, parallelization_callback = prep_refresh_parallel(samizdats, matviews, refreshes)
        drain(executor(refreshes(firstlevel), args, None, parallelization_callback=parallelization_callback))
    else:
        drain(executor(refreshes(matviews), args, cursor))

    txi_finalize(cursor, args)


def prep_refresh_parallel(samizdats, matviews, refreshes):
    deps_closure = {
        sd: {d for d in deps if d in matviews}
        for sd, deps in deps_on_closure(samizdats).items()
        if sd in matviews
    }

    depfree = {sd for sd, deps in deps_closure.items() if not deps}
    done = set()
    submitted = set(depfree)

    def paralellization_callback(sd):
        nonlocal submitted
        done.add(sd)
        left_todo = (deps_closure.keys() - done) - submitted
        if not left_todo:
            return False  # signal that we're done
        submittables = {sd for sd in left_todo if deps_closure[sd].issubset(done)}
        submitted |= submittables
        return refreshes(submittables)

    return depfree, paralellization_callback


def cmd_sync(args):
    if args.parallel and args.txdiscipline != txstyle.CHECKPOINT.value:
        raise WrongTransactionStyleForParallelRefresh()

    cursor = get_cursor(args)
    samizdats = depsort_with_sidekicks(sanity_check(get_samizdats(args.samizdatmodules)))
    issame, excess_dbstate, excess_definedstate = dbstate_equals_definedstate(cursor, samizdats)
    if issame:
        vprint(args, "No differences, nothing to do.")
        return
    max_namelen = max(len(str(ds)) for ds in excess_dbstate | excess_definedstate)
    drain = get_executor_drainer(args, max_namelen=max_namelen)
    if excess_dbstate:
        def drops():
            for sd in excess_dbstate:
                yield 'drop', sd, sd.drop(if_exists=True)  # we don't know the deptree; so they may have vanished through a cascading drop of a previous object
        drain(executor(drops(), args, cursor))
        issame, excess_dbstate, excess_definedstate = dbstate_equals_definedstate(cursor, samizdats)  # again, we don't know the in-db deptree, so we need to re-read DB state as the rug may have been pulled out from under us with cascading drops
    if excess_definedstate:
        def creates():
            to_create_ids = {sd.head_id() for sd in excess_definedstate}
            for sd in samizdats:  # iterate in proper creation order
                if sd.head_id() in to_create_ids:
                    yield 'create', sd, sd.create()
                    yield 'sign', sd, sd.sign(cursor)
        drain(executor(creates(), args, cursor))

        def refreshes(subjects):
            for sd in subjects:
                yield 'refresh', sd, sd.refresh(concurrent_allowed=False)

        matviews_to_refresh = {sd for sd in excess_definedstate if sd.entity_type == entitypes.MATVIEW}
        if matviews_to_refresh:
            drain = get_executor_drainer(args, max_namelen=max_namelen, parallel=args.parallel)
            if args.parallel:
                firstlevel, parallelization_callback = prep_refresh_parallel(samizdats, matviews_to_refresh, refreshes)
                drain(executor(refreshes(firstlevel), args, None, parallelization_callback=parallelization_callback))
            else:
                drain(executor(refreshes(matviews_to_refresh), args, cursor))

    txi_finalize(cursor, args)


def cmd_diff(args):
    cursor = get_cursor(args)
    samizdats = depsort_with_sidekicks(sanity_check(get_samizdats(args.samizdatmodules)))
    issame, excess_dbstate, excess_definedstate = dbstate_equals_definedstate(cursor, samizdats)
    if issame:
        vprint(args, "No differences.")
        exit(0)

    max_namelen = max(len(str(ds)) for ds in excess_dbstate | excess_definedstate)

    def statefmt(state, prefix):
        return '\n'.join(f'%s%-17s\t%-{max_namelen}s\t%s' % (prefix, sd.entity_type.value, sd, sd.definition_hash()) for sd in sorted(state, key=lambda sd: str(sd)))
    if excess_dbstate:
        vprint(args, statefmt(excess_dbstate, 'Not in samizdats:\t'), file=sys.stdout)
    if excess_definedstate:
        vprint(args, statefmt(excess_definedstate, 'Not in database:   \t'), file=sys.stdout)
    exit(100 + (1 if excess_dbstate else 0 | 2 if excess_definedstate else 0))


def cmd_printdot(args):
    print('\n'.join(dot(depsort_with_sidekicks(sanity_check(get_samizdats(args.samizdatmodules))))))


def cmd_nuke(args, samizdats=None):
    cursor = get_cursor(args)

    def nukes():
        nonlocal samizdats
        if samizdats is None:
            samizdats = map(dbinfo_to_class, filter(lambda a: a[-1] is not None, get_dbstate(cursor)))
        for sd in samizdats:
            yield ("nuke", sd, sd.drop(if_exists=True))

    max_namelen = max(len(str(ds)) for ds in samizdats) if samizdats else 0
    drain = get_executor_drainer(args, max_namelen=max_namelen)

    drain(executor(nukes(), args, cursor))
    txi_finalize(cursor, args)


def executor(plan, args, cursor, parallelization_callback=None):

    def actually_exec(action_totake, sd, sql):
        local_cursor = get_cursor(args) if parallelization_callback else cursor  # For parallel refreshes, get a cursor on new connection (we'll get a new connection, as this is a new thread)
        starttime = monotonic()
        try:
            try:
                local_cursor.execute("BEGIN;")  # harmless if already in a tx
                local_cursor.execute(f"SAVEPOINT action_{action_totake};")
                local_cursor.execute(sql)
            except psycopg2.errors.UndefinedFunction as ouch:
                if action_totake == 'sign':
                    local_cursor.execute(f"ROLLBACK TO SAVEPOINT action_{action_totake};")  # get back to a non-error state
                    candidate_args = [c[3] for c in get_dbstate(local_cursor, which=DBObjectType.FOREIGN, entity_types=(entitypes.FUNCTION,)) if c[:2] == (sd.schema, sd.function_name)]
                    raise FunctionSignatureError(sd, candidate_args)
                raise ouch
        except psycopg2.Error as dberr:
            raise DatabaseError(f"{action_totake} failed", dberr, sd, sql)
        local_cursor.execute(f'RELEASE SAVEPOINT action_{action_totake};')
        if args.txdiscipline == txstyle.CHECKPOINT.value and action_totake != 'create':
            # only commit *after* signing, otherwise if later the signing somehow fails we'll have created an orphan DB object that we don't recognize as ours
            local_cursor.execute("COMMIT;")
        return (monotonic() - starttime, action_totake, sd, sql)

    if parallelization_callback:
        pool = ThreadPoolExecutor(cpu_count(), thread_name_prefix="dbsamizdat-refresh-")
        tasks = []
        # initial items
        for planitem in plan:
            yield (None, *planitem)
            tasks.append(pool.submit(actually_exec, *planitem))

        done = False
        completed = set()
        while not done:
            for future in as_completed(reversed(tasks)):
                if future in completed:
                    continue
                yield future.result()
                completed.add(future)
                *_, sd, _sql = future.result()
                more_to_do = parallelization_callback(sd)
                if more_to_do is False:
                    done = True
                else:
                    for planitem in more_to_do:
                        yield (None, *planitem)
                        tasks.append(pool.submit(actually_exec, *planitem))
        pool.shutdown()

    else:
        for planitem in plan:
            yield (None, *planitem)
            runtime, *_ = actually_exec(*planitem)
            yield (runtime, *planitem)


def augment_argument_parser(p, in_django=False, log_rather_than_print=True):

    def perhaps_add_modules_argument(parser):
        if not in_django:
            parser.add_argument('samizdatmodules', nargs='+', help="Names of modules containing Samizdat subclasses")

    def add_dbarg_argument(parser):
        if in_django:
            parser.add_argument('dbconn', nargs='?', default='default', help="Django DB connection key (default:'default'). If you don't know what this is, then you don't need it.")
        else:
            parser.add_argument('dburl', help="PostgreSQL DB connection string. Trivially, this might be 'postgresql:///mydbname'. See https://www.postgresql.org/docs/14/static/libpq-connect.html#id-1.7.3.8.3.6 .")

    def add_txdiscipline_argument(parser):
        parser.add_argument('--txdiscipline', '-t', choices=(txstyle.CHECKPOINT.value, txstyle.JUMBO.value, txstyle.DRYRUN.value), default=txstyle.CHECKPOINT.value, help=f"""Transaction discipline. The default "{txstyle.CHECKPOINT.value}" level commits after every dbsamizdat-level action, and is compatible with parallelized materialized view refreshing. "{txstyle.JUMBO.value}" creates one large transaction. "{txstyle.DRYRUN.value}" also creates one large transaction, but rolls it back.""")

    def add_parallel_argument(parser):
        parser.add_argument('--parallel', '-p', action="store_true", help=f'Parallelize refreshing of materialized views. Can only be used with the "{txstyle.CHECKPOINT.value}" transaction discipline.')

    p.set_defaults(
        func=lambda whatevs: p.print_help(),
        in_django=in_django,
        log_rather_than_print=log_rather_than_print,
        samizdatmodules=[],
        verbosity=1,
        parallel=False,
    )
    if not in_django:
        p.add_argument('--quiet', '-q', help="Be quiet (minimal output)", action="store_const", const=0, dest='verbosity')
        p.add_argument('--verbose', '-v', help="Be verbose (on stderr).", action="store_const", const=2, dest='verbosity')
    else:
        p.add_argument('-v', '--verbosity', default=1, type=int)
    subparsers = p.add_subparsers(title='commands')

    p_nuke = subparsers.add_parser('nuke', help='Drop all dbsamizdat database objects.')
    p_nuke.set_defaults(func=cmd_nuke)
    add_txdiscipline_argument(p_nuke)
    add_dbarg_argument(p_nuke)

    p_printdot = subparsers.add_parser('printdot', help='Print DB object dependency tree in GraphViz format.')
    p_printdot.set_defaults(func=cmd_printdot)
    perhaps_add_modules_argument(p_printdot)

    p_diff = subparsers.add_parser('diff', help='Show differences between dbsamizdat state and database state. Exits nonzero if any are found: 101 when there are excess DB-side objects, 102 if there are excess python-side objects, 103 if both sides have excess objects.')
    p_diff.set_defaults(func=cmd_diff)
    add_dbarg_argument(p_diff)
    perhaps_add_modules_argument(p_diff)

    p_refresh = subparsers.add_parser('refresh', help='Refresh materialized views, in dependency order.')
    p_refresh.set_defaults(func=cmd_refresh)
    add_txdiscipline_argument(p_refresh)
    add_parallel_argument(p_refresh)
    add_dbarg_argument(p_refresh)
    perhaps_add_modules_argument(p_refresh)
    p_refresh.add_argument('--belownodes', '-b', nargs='*', help="Limit to views that depend on ENTITYNAMES (usually, specific tables).", metavar='ENTITYNAMES')

    p_sync = subparsers.add_parser('sync', help='Make it so!')
    p_sync.set_defaults(func=cmd_sync)
    add_txdiscipline_argument(p_sync)
    add_parallel_argument(p_sync)
    add_dbarg_argument(p_sync)
    perhaps_add_modules_argument(p_sync)


def main():
    p = argparse.ArgumentParser(description='dbsamizdat, the blissfully naive PostgreSQL database object manager.')
    augment_argument_parser(p, log_rather_than_print=False)
    args = p.parse_args()
    try:
        args.func(args)
    except SamizdatException as argh:
        exit(f'\n\n\nFATAL: {argh}')
    except KeyboardInterrupt:
        exit('\nInterrupted.')


if __name__ == '__main__':
    main()
