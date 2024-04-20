from typing import Callable, Iterable
import logging
import datetime
import pytz

logger = logging.getLogger(__name__)

StringProvider = str | Callable[[], str]
StringByIndexProvider = str | Callable[[int], str]
StringChoiceProvider = str | Callable[[Iterable[str]], str]
IntProvider = int | Callable[[], int]
FloatProvider = float | Callable[[], float]
DictProvider = dict | Callable[[], dict]
FilePathProvider = StringProvider
DateTimeProvider = datetime.datetime | Callable[[], datetime.datetime]

def resolve(
    provider,
    default=None,
    *args
):
    if callable(provider):
        ret = provider(*args)

    else:
        ret = provider

    if ret is None and default is not None:
        return default

    return ret


def try_resolve(
        provider,
        *args):
    try:
        return resolve(provider, *args)
    except:
        logger.error(f"Unable to resolve provider: {provider}")
        return None

def resolve_string_provider(
        string_provider: StringProvider
) -> str:
    return resolve(string_provider)


def resolve_string_by_index_provider(
        string_by_index_provider: StringByIndexProvider,
        index: int
) -> str:
    return resolve(string_by_index_provider,
                   index)

def resolve_string_by_choice_provider(
        string_choice_provider: StringChoiceProvider,
        choices: Iterable[str]
) -> str:
    return resolve(string_choice_provider,
                   choices)

def resolve_dict_provider(
        dict: DictProvider
) -> dict:
    return resolve(dict)


def resolve_int_provider(
        int_provider: IntProvider
) -> int:
    return resolve(int_provider)

def resolve_float_provider(
        float_provider: FloatProvider
) -> float:
    return resolve(float_provider)

def resolve_datetime_provider(
    datetime_provider: DateTimeProvider,
    default_now: bool = False,
    as_utc: bool = False
) -> datetime.datetime:
    ret = resolve(datetime_provider)

    if ret is None and default_now:
        ret = datetime.datetime.now()

    if ret is None:
        return None

    if as_utc:
        ret = ret.astimezone(pytz.utc)

    return ret