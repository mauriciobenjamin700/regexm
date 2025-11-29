"""
CPF Validation and Formatting Functions

This module provides functions to validate and format Brazilian CPF
(Cadastro de Pessoa Física).
"""

import re


def format_cpf(cpf: str) -> str:
    """
    Formats a CPF string to the standard Brazilian format (XXX.XXX.XXX-XX).

    Args:
        cpf (str): CPF string with or without formatting

    Returns:
        str: Formatted CPF string if it has 11 digits, otherwise returns the
        cleaned input

    Example:
        - format_cpf("12345678901")  # Returns: "123.456.789-01"
        - format_cpf("123.456.789-01")  # Returns: "123.456.789-01"
        - format_cpf("1234567890")  # Returns: "1234567890"
    """
    cpf = re.sub(r"\D", "", cpf)

    # Aplica a máscara se tiver 11 dígitos
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf


def validate_cpf(cpf: str) -> bool:
    """
    Validates a Brazilian CPF (Cadastro de Pessoa Física).

    Args:
        cpf (str): CPF string to validate

    Returns:
        bool: True if CPF is valid, False otherwise

    Example:
        - validate_cpf("123.456.789-09")  # Returns: False
        - validate_cpf("111.444.777-35")  # Returns: True
        - validate_cpf("12345678909")  # Returns: False
        - validate_cpf("11144477735")  # Returns: True
    """
    cpf = re.sub(r"\D", "", cpf)

    # CPF deve ter 11 dígitos e não pode ter todos os dígitos iguais
    if len(cpf) != 11 or re.match(r"^(\d)\1+$", cpf):
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto in [10, 11]:
        resto = 0
    if resto != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto in [10, 11]:
        resto = 0

    return resto == int(cpf[10])


def is_cpf_format(cpf: str) -> bool:
    """
    Checks if the string has a valid CPF format (with or without formatting).

    Args:
        cpf (str): String to check

    Returns:
        bool: True if string has CPF format, False otherwise

    Example:
        - is_cpf_format("123.456.789-01")  # Returns: True
        - is_cpf_format("12345678901")  # Returns: True
        - is_cpf_format("1234567890")  # Returns: False
    """
    clean_cpf = re.sub(r"\D", "", cpf)
    return len(clean_cpf) == 11 and clean_cpf.isdigit()
