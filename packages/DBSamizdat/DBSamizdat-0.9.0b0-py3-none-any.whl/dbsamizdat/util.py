from psycopg2.extensions import cursor as PGcursor


def fqify_node(node):
    """
    normalize node names to (schema, nodename) format, assuming the 'public' schema for not-fully-qualified node names
    """
    if isinstance(node, str):
        firstpart, *rest = node.split('.', maxsplit=1)
        if rest:
            return (firstpart, rest[0])
        return ("public", firstpart)
    return node


def nodenamefmt(node):
    """
    format node for presentation purposes. If it's in the public schema, omit the "public" for brevity.
    """
    if isinstance(node, str):
        return node
    if isinstance(node, tuple):
        schema, name, *args = node
        identifier = f"{schema}.{name}" if schema not in {'public', None} else name
        if args and args[0]:
            return f'{identifier}({args[0]})'
        return identifier
    return str(node)  # then it should be a Samizdat


def db_object_identity(thing):
    schema, name, *fnargs = fqify_node(thing)
    args = f'({fnargs[0]})' if fnargs else ''
    return '"%s"."%s"%s' % (schema, name, args)


def sqlfmt(sql: str):
    return '\n'.join(('\t\t' + line for line in sql.splitlines()))


def honest_cursor(cursor) -> PGcursor:
    """
    Sometimes you need the real PsycoPG cursor instead of proxy objects (Django cursor, or a DebugCursor underneath, ...)
    This will try to dig down to the real cursor, returning it.
    """
    if isinstance(cursor, PGcursor):
        return cursor
    try:
        return honest_cursor(cursor.cursor)
    except AttributeError:
        raise ValueError("Quest for an actual PsycoPG cursor was unfruitful :-/")
