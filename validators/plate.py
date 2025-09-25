"""
Vehicle Plate Validation Functions

This module provides functions to validate Brazilian vehicle plates
(both old format and Mercosul format).
"""

import re


def validate_plate(plate: str) -> bool:
    """
    Validates a Brazilian vehicle plate (both old and Mercosul formats).

    Old format: AAA-0000 (3 letters + 4 digits)
    Mercosul format: AAA0A00 (3 letters + 1 digit + 1 letter + 2 digits)

    Args:
        plate (str): Plate string to validate

    Returns:
        bool: True if plate is valid, False otherwise
    """
    # Remove espaços e hífens, converte para maiúsculo
    limpo = re.sub(r"[\s\-]", "", plate).upper()

    # Padrão antigo (AAA0000)
    old_pattern = r"^[A-Z]{3}\d{4}$"

    # Padrão Mercosul (AAA0A00)
    mercosul_pattern = r"^[A-Z]{3}\d[A-Z]\d{2}$"

    return bool(re.match(old_pattern, limpo)) or bool(
        re.match(mercosul_pattern, limpo)
    )


def format_plate(plate: str, format_type: str = "clean") -> str:
    """
    Formats a vehicle plate string.

    Args:
        plate (str): Plate string to format
        format_type (str): 'clean' (remove formatting) or 'dash' (add dash)

    Returns:
        str: Formatted plate string
    """
    # Remove espaços e hífens, converte para maiúsculo
    clean_plate = re.sub(r"[\s\-]", "", plate).upper()

    if format_type == "dash" and len(clean_plate) >= 7:
        # Adiciona hífen no formato antigo (AAA-0000)
        if re.match(r"^[A-Z]{3}\d{4}$", clean_plate):
            return f"{clean_plate[:3]}-{clean_plate[3:]}"
        # Para Mercosul, também pode usar hífen
        elif re.match(r"^[A-Z]{3}\d[A-Z]\d{2}$", clean_plate):
            return f"{clean_plate[:3]}-{clean_plate[3:]}"

    return clean_plate


def is_old_format_plate(plate: str) -> bool:
    """
    Checks if the plate follows the old Brazilian format (AAA-0000).

    Args:
        plate (str): Plate string to check

    Returns:
        bool: True if plate follows old format, False otherwise
    """
    limpo = re.sub(r"[\s\-]", "", plate).upper()
    return bool(re.match(r"^[A-Z]{3}\d{4}$", limpo))


def is_mercosul_format_plate(plate: str) -> bool:
    """
    Checks if the plate follows the Mercosul format (AAA0A00).

    Args:
        plate (str): Plate string to check

    Returns:
        bool: True if plate follows Mercosul format, False otherwise
    """
    limpo = re.sub(r"[\s\-]", "", plate).upper()
    return bool(re.match(r"^[A-Z]{3}\d[A-Z]\d{2}$", limpo))
