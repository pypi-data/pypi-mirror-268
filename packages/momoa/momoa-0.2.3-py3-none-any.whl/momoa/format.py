"""Helper utilities for formatting serialized data."""

from datetime import date, datetime
from ipaddress import ip_address
from typing import Any, Callable, cast, Mapping
from uuid import UUID

from dateutil.parser import isoparse

FormatMapping = Mapping[str, Callable]


def _format_date_time(value: datetime) -> str:
    """
    Helper function for formatting date-time values.

    If all the sub-day units are set to `00`, the value is formatted as a date.
    """
    if not any((value.hour, value.minute, value.second, value.microsecond)):
        value = cast(datetime, date(value.year, value.month, value.day))
    return value.isoformat()


class StringFormat:
    """
    Helper utility for converting values of string fields with format.

    JSON Schema `string` type supports the `format` keyword, which can be used to
    convert its value to and from a native Python type. This class supports custom
    implementation of that conversion.
    """

    _to_mapping: FormatMapping = {"date-time": _format_date_time}
    _from_mapping: FormatMapping = {
        "date-time": isoparse,
        "ipv4": ip_address,
        "ipv6": ip_address,
        "uuid": UUID,
    }

    def __init__(self, fmt):
        self.format = fmt

    def to_(self, value: Any) -> str:
        """
        Converts a value of a Python native type to a formatted JSON string.

        Args:
            value: Any Python type, to be converted if supported.

        Returns:
            A formatted string.
        """
        return self._to_mapping.get(self.format, str)(value)

    def from_(self, value: str) -> Any:
        """
        Converts a formatted JSON string to a native Python type.

        Args:
            value: A formatted string, to be converted if supported.

        Returns:
            A native Python type if conversion is supported, or the original
            string value if not.
        """
        return self._from_mapping.get(self.format, str)(value)
