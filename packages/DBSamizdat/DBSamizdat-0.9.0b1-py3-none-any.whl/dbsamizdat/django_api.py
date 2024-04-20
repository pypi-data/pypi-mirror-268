"""
API for using dbsamizdat as a library in Django
"""

from argparse import Namespace as _Namespace
from typing import Iterable, Union

from .runner import cmd_refresh as _cmd_refresh, cmd_sync as _cmd_sync, cmd_nuke as _cmd_nuke, txstyle
from .samizdat import Samizdat
from .exceptions import WrongTransactionStyleForParallelRefresh

_CMD_ARG_DEFAULTS = dict(
    in_django=True,
    verbosity=1,
    log_rather_than_print=True,
    parallel=False,
)


def refresh(
    dbconn: str = 'default',
    transaction_style: txstyle = txstyle.CHECKPOINT,
    belownodes: Iterable[Union[str, tuple, Samizdat]] = tuple(),
    samizdatmodules=tuple(),
    parallel=False,
):
    """
    Refresh materialized views, in dependency order, optionally parallelized (where the dependency tree allows), optionally restricted to views depending directly or transitively on any of the DB objects specified in `belownodes`.
    """
    if parallel and transaction_style != txstyle.CHECKPOINT:
        raise WrongTransactionStyleForParallelRefresh()
    args = _Namespace(
        **{
            **_CMD_ARG_DEFAULTS,
            'dbconn': dbconn,
            'txdiscipline': transaction_style.value,
            'belownodes': belownodes,
            'samizdatmodules': samizdatmodules,
            'parallel': parallel,
        }
    )
    _cmd_refresh(args)


def sync(
    dbconn: str = 'default',
    transaction_style: txstyle = txstyle.JUMBO,
    samizdatmodules=tuple(),
    parallel=False,
):
    """
    Sync dbsamizdat state to the DB.
    """
    if parallel and transaction_style != txstyle.CHECKPOINT:
        raise WrongTransactionStyleForParallelRefresh()
    args = _Namespace(
        **{
            **_CMD_ARG_DEFAULTS,
            'dbconn': dbconn,
            'txdiscipline': transaction_style.value,
            'samizdatmodules': samizdatmodules,
            'parallel': parallel,
        }
    )
    _cmd_sync(args)


def nuke(
    dbconn: str = 'default',
    transaction_style: txstyle = txstyle.JUMBO,
    samizdatmodules=tuple(),
):
    """
    Remove any database object tagged as samizdat.
    """
    args = _Namespace(
        **_CMD_ARG_DEFAULTS,
        dbconn=dbconn,
        txdiscipline=transaction_style.value,
        samizdatmodules=samizdatmodules,
    )
    _cmd_nuke(args)
