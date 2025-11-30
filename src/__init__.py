"""
Root package for regexm validators

This package provides various validation and formatting functions for
Brazilian-specific data types such as CNH (driver's license),
CPF (individual taxpayer registry), CRV (vehicle registration certificate),
email addresses, passwords, phone numbers, and vehicle license plates

Functions:
- CNH:
  - `format_cnh`,
  - `is_cnh_format`,
  - `validate_cnh`
- CPF:
  - `format_cpf`,
  - `is_cpf_format`,
  - `validate_cpf`
- CRV:
  - `format_crv`,
  - `is_crv_format`,
  - `validate_crv`
- Email:
  - `extract_domain`,
  - `extract_username`,
  - `is_email_format`,
  - `validate_email`
- Password:
  - `validate_password_length`,
  - `validate_password_match`,
  - `validate_password_strength`
- Phone:
  - `clean_phone`,
  - `format_brazilian_phone`,
  - `is_valid_ddd`,
  - `validate_brazilian_phone`
- Plate:
  - `format_plate`,
  - `is_mercosul_format_plate`,
  - `is_old_format_plate`,
  - `validate_plate`

"""

from .cnh import format_cnh, is_cnh_format, validate_cnh
from .cpf import format_cpf, is_cpf_format, validate_cpf
from .crv import format_crv, is_crv_format, validate_crv
from .email import (
    extract_domain,
    extract_username,
    is_email_format,
    validate_email,
)
from .password import (
    validate_password_length,
    validate_password_match,
    validate_password_strength,
)
from .phone import (
    clean_phone,
    format_brazilian_phone,
    is_valid_ddd,
    validate_brazilian_phone,
)
from .plate import (
    format_plate,
    is_mercosul_format_plate,
    is_old_format_plate,
    validate_plate,
)

__all__ = [
    # CNH
    "validate_cnh",
    "format_cnh",
    "is_cnh_format",
    # CPF
    "format_cpf",
    "validate_cpf",
    "is_cpf_format",
    # CRV
    "validate_crv",
    "format_crv",
    "is_crv_format",
    # Email
    "validate_email",
    "is_email_format",
    "extract_domain",
    "extract_username",
    # Password
    "validate_password_length",
    "validate_password_strength",
    "validate_password_match",
    # Phone
    "format_brazilian_phone",
    "validate_brazilian_phone",
    "clean_phone",
    "is_valid_ddd",
    # Plate
    "validate_plate",
    "format_plate",
    "is_old_format_plate",
    "is_mercosul_format_plate",
]

__annotations__ = {
    "CNH": {
        "format_cnh": "Function to format CNH numbers",
        "is_cnh_format": "Function to check CNH format",
        "validate_cnh": "Function to validate CNH numbers",
    },
    "CPF": {
        "format_cpf": "Function to format CPF numbers",
        "is_cpf_format": "Function to check CPF format",
        "validate_cpf": "Function to validate CPF numbers",
    },
    "CRV": {
        "format_crv": "Function to format CRV numbers",
        "is_crv_format": "Function to check CRV format",
        "validate_crv": "Function to validate CRV numbers",
    },
    "Email": {
        "extract_domain": "Function to extract domain from email",
        "extract_username": "Function to extract username from email",
        "is_email_format": "Function to check email format",
        "validate_email": "Function to validate email addresses",
    },
    "Password": {
        "validate_password_length": "Function to validate password length",
        "validate_password_match": "Function to check if passwords match",
        "validate_password_strength": "Function to validate password strength",
    },
    "Phone": {
        "clean_phone": "Function to clean phone number input",
        "format_brazilian_phone": "Function to format Brazilian phone",
        "is_valid_ddd": "Function to check valid DDD codes",
        "validate_brazilian_phone": "Function to validate Brazilian phone",
    },
    "Plate": {
        "format_plate": "Function to format vehicle license plates",
        "is_mercosul_format_plate": "Function to check Mercosul plate format",
        "is_old_format_plate": "Function to check old plate format",
        "validate_plate": "Function to validate vehicle license plates",
    },
}
