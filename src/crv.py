"""
CRV (Certificado de Registro de Veículo) Validation Functions

This module provides functions to validate Brazilian CRV.
"""

import re


def validate_crv(crv: str) -> bool:
    """
    Validates a Brazilian CRV (Certificado de Registro de Veículo).

    Args:
        crv (str): CRV string to validate

    Returns:
        bool: True if CRV is valid, False otherwise

    Example:
        - validate_crv("A1B2C3D4E5F")  # Returns: True
        - validate_crv("1234567890")  # Returns: False
        - validate_crv("A1B2 C3D4E5F")  # Returns: True
    """
    # Remove espaços e converte para maiúsculo
    limpo = re.sub(r"\s", "", crv).upper()

    # CRV deve ter 11 caracteres alfanuméricos
    return bool(re.match(r"^[A-Z0-9]{11}$", limpo))


def format_crv(crv: str) -> str:
    """
    Formats a CRV string by removing spaces and converting to uppercase.

    Args:
        crv (str): CRV string to format

    Returns:
        str: Formatted CRV string

    Example:
        - format_crv("a1b2 c3d4e5f")  # Returns: "A1B2C3D4E5F"
        - format_crv("A1B2C3D4E5F")  # Returns: "A1B2C3D4E5F"
        - format_crv("  a1 b2 c3 d4 e5 f  ")  # Returns: "A1B2C3D4E5F"
    """
    return re.sub(r"\s", "", crv).upper()


def is_crv_format(crv: str) -> bool:
    """
    Checks if the string has a valid CRV format.

    Args:
        crv (str): String to check

    Returns:
        bool: True if string has CRV format, False otherwise

    Example:
        - is_crv_format("A1B2C3D4E5F")  # Returns: True
        - is_crv_format("1234567890")  # Returns: False
        - is_crv_format("A1B2 C3D4E5F")  # Returns: True
    """
    clean_crv = re.sub(r"\s", "", crv).upper()
    return len(clean_crv) == 11 and bool(
        re.match(r"^[A-Z0-9]{11}$", clean_crv)
    )
