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
    """
    return re.sub(r"\s", "", crv).upper()


def is_crv_format(crv: str) -> bool:
    """
    Checks if the string has a valid CRV format.

    Args:
        crv (str): String to check

    Returns:
        bool: True if string has CRV format, False otherwise
    """
    clean_crv = re.sub(r"\s", "", crv).upper()
    return len(clean_crv) == 11 and bool(
        re.match(r"^[A-Z0-9]{11}$", clean_crv)
    )
