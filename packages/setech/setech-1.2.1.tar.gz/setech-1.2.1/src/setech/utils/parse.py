import dataclasses
import datetime
import decimal
import json
import warnings
from typing import Any

from pydantic import BaseModel

from setech.utils.warnings import deprecated

__all__ = [
    "SetechJSONEncoder",
    "as_decimal",
    "as_decimal_or_none",
    "jsonify_value",
    "shorten_value",
    "shortify_log_extra_data",
    "str_as_date",
    "str_as_date_or_none",
]


def str_as_date(date_str: str, date_format: str = "%Y-%m-%d") -> datetime.date:
    datetime_object = datetime.datetime.strptime(date_str, date_format)
    return datetime_object.date()


def str_as_date_or_none(date_str: str | None, date_format: str = "%Y-%m-%d") -> datetime.date | None:
    if not isinstance(date_str, str):
        return None
    try:
        return str_as_date(date_str, date_format)
    except (ValueError, TypeError):
        return None


def as_decimal(decimal_str: str | int | float) -> decimal.Decimal:
    return decimal.Decimal(str(decimal_str))


def as_decimal_or_none(decimal_str: str | int | float | None) -> decimal.Decimal | None:
    if not isinstance(decimal_str, (str | int | float)):
        return None
    try:
        return as_decimal(decimal_str)
    except (decimal.DecimalException, TypeError):
        return None


def jsonify_value(value: Any) -> Any:
    """Return JSON'ified version of the object type-casted using SetechJSONEncoder

    :param value: any object
    :return: json compatible object
    """
    return json.loads(json.dumps(value, cls=SetechJSONEncoder))


class SetechJSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        try:
            if isinstance(obj, decimal.Decimal):
                return str(obj)
            if isinstance(obj, (datetime.datetime, datetime.date)):
                return obj.isoformat()
            if isinstance(obj, BaseModel):
                return obj.model_dump()
            if isinstance(obj, datetime.timedelta):
                return dict(__type__="timedelta", total_seconds=obj.total_seconds())
            if isinstance(obj, set):
                return sorted(obj, key=str)
            if hasattr(obj, "as_dict"):
                return obj.as_dict
            if dataclasses.is_dataclass(obj):
                return dataclasses.asdict(obj)
            if hasattr(obj, "__dict__"):
                return obj.__dict__
            return super().default(obj)
        except TypeError as exc:
            if "not JSON serializable" in str(exc):
                return str(obj)
            raise exc  # pragma: no cover


def shorten_value(value: Any) -> Any:
    """Recursively shorten long string values and return a shortened version copy object.

    :param value: Object in which to recursively search for strings to shorten
    :return: Shortened version of the value
    """
    if isinstance(value, str):
        return f"{value[:30]}...{value[-30:]}" if isinstance(value, str) and len(value) > 64 else value
    if isinstance(value, list):
        return [shorten_value(v) for v in value]
    if isinstance(value, tuple):
        return tuple(shorten_value(v) for v in value)
    if isinstance(value, dict):
        return {k: shorten_value(v) for k, v in value.items()}
    return value


def shortify_log_extra_data(log_value: Any) -> dict[str, Any]:
    """Shorten long values and normalize (to json compatible format) dictionary values

    :param log_value: Object to convert into json log favourable format
    :return: shortened and normalized object
    """
    shortened_log_value = shorten_value(jsonify_value(log_value))
    if not isinstance(shortened_log_value, dict):
        shortened_log_value = {"extra_data": shortened_log_value}
    return shortened_log_value


@deprecated(new_method=shortify_log_extra_data)
def shortify_log_dict(dct: Any) -> dict[str, Any]:
    warnings.warn("Deprecated method name! Use `shortify_log_extra_data` instead", DeprecationWarning, 2)
    return shortify_log_extra_data(dct)
