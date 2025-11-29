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
    cleaned = re.sub(r"\D", "", cnh)

    return bool(re.match(r"^\d{11}$", cleaned))


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
    clean_cnh = re.sub(r"\D", "", cnh)
    return len(clean_cnh) == 11 and clean_cnh.isdigit()
