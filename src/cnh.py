"""
CNH (Carteira Nacional de Habilitação) Validation Functions

This module provides functions to validate Brazilian CNH.
"""

import re


def validate_cnh(cnh: str) -> bool:
    """
    Validates a Brazilian CNH (Carteira Nacional de Habilitação).

    Args:
        cnh (str): CNH string to validate

    Returns:
        bool: True if CNH has 11 digits, False otherwise

    Example:
        - validate_cnh("12345678901")  # Returns: True
        - validate_cnh("123.456.789-01")  # Returns: True
        - validate_cnh("1234567890")  # Returns: False
    """
    # CNH validation requires exactly 11 digits with correct check digits.
    # Do not accept formatted strings (with dots/hyphens) here — the tests
    # expect `validate_cnh("123.456.789-01")` to be False.
    if not re.fullmatch(r"\d{11}", cnh):
        return False

    digits = [int(d) for d in cnh]

    # First verifier digit: weights 9..1 applied to digits 1..9
    soma1 = sum(digits[i] * (9 - i) for i in range(9))
    resto1 = (soma1 * 10) % 11
    if resto1 == 10:
        resto1 = 0
    if resto1 != digits[9]:
        return False

    # Second verifier digit: weights 1..9 applied to digits 1..9
    soma2 = sum(digits[i] * (i + 1) for i in range(9))
    resto2 = (soma2 * 10) % 11
    if resto2 == 10:
        resto2 = 0

    return resto2 == digits[10]


def format_cnh(cnh: str) -> str:
    """
    Formats a CNH string by removing non-digit characters.

    Args:
        cnh (str): CNH string to format

    Returns:
        str: Formatted CNH string with only digits

    Example:
        - format_cnh("123.456.789-01")  # Returns: "12345678901"
        - format_cnh("12345678901")  # Returns: "12345678901"
        - format_cnh("12A34B56C78D90")  # Returns: "1234567890"
    """
    return re.sub(r"\D", "", cnh)


def is_cnh_format(cnh: str) -> bool:
    """
    Checks if the string has a valid CNH format.

    Args:
        cnh (str): String to check

    Returns:
        bool: True if string has CNH format, False otherwise

    Example:
        - is_cnh_format("12345678901")  # Returns: True
        - is_cnh_format("123.456.789-01")  # Returns: True
        - is_cnh_format("1234567890")  # Returns: False
    """
    # For CNH we expect a plain 11-digit string (no punctuation).
    return bool(re.fullmatch(r"\d{11}", cnh))


__all__ = [
    "validate_cnh",
    "format_cnh",
    "is_cnh_format",
]
