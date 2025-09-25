"""
Regex Library - Brazilian Document and Data Validators

This package provides comprehensive validation functions for Brazilian documents
and common data types used in web applications and forms.
"""

from .validators.cpf import validate_cpf, format_cpf, is_cpf_format
from .validators.crv import validate_crv, format_crv, is_crv_format
from .validators.cnh import validate_cnh, format_cnh, is_cnh_format
from .validators.plate import (
    validate_plate, format_plate, is_old_format_plate, is_mercosul_format_plate
)
from .validators.email import (
    validate_email, is_email_format, extract_domain, extract_username
)
from .validators.phone import (
    format_brazilian_phone, validate_brazilian_phone, 
    clean_phone, is_valid_ddd
)
from .validators.password import (
    validate_password_length, validate_password_strength, 
    validate_password_match
)
from .validators.driver import validate_driver_data, validate_driver_data_simple
from .validators.user import validate_user_data, validate_user_data_simple

__version__ = "1.0.0"
__author__ = "Maurício Benjamim"

__all__ = [
    # CPF functions
    'validate_cpf',
    'format_cpf', 
    'is_cpf_format',
    
    # CRV functions
    'validate_crv',
    'format_crv',
    'is_crv_format',
    
    # CNH functions
    'validate_cnh',
    'format_cnh',
    'is_cnh_format',
    
    # Plate functions
    'validate_plate',
    'format_plate',
    'is_old_format_plate',
    'is_mercosul_format_plate',
    
    # Email functions
    'validate_email',
    'is_email_format',
    'extract_domain',
    'extract_username',
    
    # Phone functions
    'format_brazilian_phone',
    'validate_brazilian_phone',
    'clean_phone',
    'is_valid_ddd',
    
    # Password functions
    'validate_password_length',
    'validate_password_strength',
    'validate_password_match',
    
    # Combined validation functions
    'validate_driver_data',
    'validate_driver_data_simple',
    'validate_user_data',
    'validate_user_data_simple',
]