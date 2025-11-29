"""
Phone Number Validation and Formatting Functions

This module provides functions to validate and format Brazilian phone numbers.
"""

import re


def format_brazilian_phone(phone: str) -> str:
    """
    Formats a phone number to the Brazilian cell phone standard.
    Always forces "9" after the area code. Ex: (11) 91234-5678

    Args:
        phone (str): Phone string with numbers or mixed text

    Returns:
        str: Formatted phone string: (XX) 9XXXX-XXXX

    Example:
        - format_brazilian_phone("11912345678")  # Returns: "(11) 91234-5678"
        - format_brazilian_phone("(21) 98765-4321")#Returns: "(21) 99876-5432"
        - format_brazilian_phone("1234")  # Returns: "12 934-1234"
    """
    # Remove tudo que não for número
    digits = re.sub(r"\D", "", phone)[:11]  # máximo 11 dígitos

    # Se tiver menos que 2 dígitos, não tenta formatar ainda
    if len(digits) < 2:
        return digits

    ddd = digits[:2]
    rest = digits[2:]

    # Garante que o número comece com "9"
    if rest and rest[0] != "9":
        rest = "9" + rest

    # Limita para 9 dígitos no número após o DDD
    rest = rest[:9]

    prefix = rest[:5]
    suffix = rest[5:]

    result = f"({ddd})"

    if prefix:
        result += f" {prefix}"
    if suffix:
        result += f"-{suffix}"

    return result.strip()


def validate_brazilian_phone(phone: str) -> bool:
    """
    Validates a Brazilian phone number.

    Args:
        phone (str): Phone number to validate

    Returns:
        bool: True if phone number is valid (10 or 11 digits), False otherwise

    Example:
        - validate_brazilian_phone("11912345678")  # Returns: True
        - validate_brazilian_phone("(21) 98765-4321")  # Returns: True
        - validate_brazilian_phone("1234")  # Returns: False
    """
    digits = re.sub(r"\D", "", phone)
    # Accept both 10 digits (will add 9) and 11 digits
    return len(digits) in [10, 11]


def clean_phone(phone: str) -> str:
    """
    Cleans a phone number by removing all non-digit characters.

    Args:
        phone (str): Phone number to clean

    Returns:
        str: Phone number with only digits

    Example:
        - clean_phone("(11) 91234-5678")  # Returns: "11912345678"
        - clean_phone("21 98765 4321")  # Returns: "21987654321"
        - clean_phone("1234")  # Returns: "1234"
    """
    return re.sub(r"\D", "", phone)


def is_valid_ddd(ddd: str) -> bool:
    """
    Validates if the DDD (area code) is valid for Brazil.

    Args:
        ddd (str): Two-digit area code

    Returns:
        bool: True if DDD is valid, False otherwise

    Example:
        - is_valid_ddd("11")  # Returns: True
        - is_valid_ddd("99")  # Returns: True
        - is_valid_ddd("00")  # Returns: False
    """
    valid_ddds = {
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",  # São Paulo
        "21",
        "22",
        "24",  # Rio de Janeiro
        "27",
        "28",  # Espírito Santo
        "31",
        "32",
        "33",
        "34",
        "35",
        "37",
        "38",  # Minas Gerais
        "41",
        "42",
        "43",
        "44",
        "45",
        "46",  # Paraná
        "47",
        "48",
        "49",  # Santa Catarina
        "51",
        "53",
        "54",
        "55",  # Rio Grande do Sul
        "61",  # Distrito Federal
        "62",
        "64",  # Goiás
        "63",  # Tocantins
        "65",
        "66",  # Mato Grosso
        "67",  # Mato Grosso do Sul
        "68",  # Acre
        "69",  # Rondônia
        "71",
        "73",
        "74",
        "75",
        "77",  # Bahia
        "79",  # Sergipe
        "81",
        "87",  # Pernambuco
        "82",  # Alagoas
        "83",  # Paraíba
        "84",  # Rio Grande do Norte
        "85",
        "88",  # Ceará
        "86",
        "89",  # Piauí
        "91",
        "93",
        "94",  # Pará
        "92",
        "97",  # Amazonas
        "95",  # Roraima
        "96",  # Amapá
        "98",
        "99",  # Maranhão
    }
    return ddd in valid_ddds
