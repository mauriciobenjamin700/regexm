"""
Test Suite for Brazilian Document Validators

Run: python3 test_validators.py
"""

import sys
import traceback
from validators.cpf import validate_cpf
from validators.crv import validate_crv
from validators.cnh import validate_cnh
from validators.plate import validate_plate, is_old_format_plate, is_mercosul_format_plate
from validators.email import validate_email
from validators.phone import validate_brazilian_phone, format_brazilian_phone
from validators.password import validate_password_length, validate_password_strength


def test_cpf():
    """Test CPF validation with known cases."""
    print("Testing CPF validation...")
    
    # Valid CPFs (these are test CPFs, not real ones)
    valid_tests = [
        ("11144477735", True),
        ("111.444.777-35", True),
    ]
    
    # Invalid CPFs
    invalid_tests = [
        ("11111111111", False),  # All same digits
        ("123.456.789-00", False),  # Invalid check digits
        ("123", False),  # Too short
        ("", False),  # Empty
    ]
    
    all_passed = True
    
    for cpf, expected in valid_tests + invalid_tests:
        result = validate_cpf(cpf)
        if result != expected:
            print(f"  ❌ CPF {cpf}: expected {expected}, got {result}")
            all_passed = False
        else:
            print(f"  ✅ CPF {cpf}: {result}")
    
    return all_passed


def test_phone():
    """Test phone validation and formatting."""
    print("Testing phone validation...")
    
    tests = [
        ("11987654321", True, "(11) 98765-4321"),
        ("(11) 98765-4321", True, "(11) 98765-4321"),
        ("11 98765-4321", True, "(11) 98765-4321"),
        ("1187654321", True, "(11) 98765-4321"),  # Adds 9
        ("123", False, "(12) 93"),  # Too short, but formats what it can
        ("", False, ""),
    ]
    
    all_passed = True
    
    for phone, valid_expected, format_expected in tests:
        # Test validation
        valid_result = validate_brazilian_phone(phone)
        if valid_result != valid_expected:
            print(f"  ❌ Phone {phone} validation: expected {valid_expected}, got {valid_result}")
            all_passed = False
        
        # Test formatting
        format_result = format_brazilian_phone(phone)
        if format_result != format_expected:
            print(f"  ❌ Phone {phone} formatting: expected '{format_expected}', got '{format_result}'")
            all_passed = False
        
        if valid_result == valid_expected and format_result == format_expected:
            print(f"  ✅ Phone {phone}: valid={valid_result}, formatted='{format_result}'")
    
    return all_passed


def test_plates():
    """Test vehicle plate validation."""
    print("Testing plate validation...")
    
    tests = [
        ("BRA2E19", True, False, True),  # valid, not old format, is mercosul
        ("BRA-2E19", True, False, True),
        ("ABC1234", True, True, False),   # valid, is old format, not mercosul
        ("ABC-1234", True, True, False),
        ("123ABCD", False, False, False), # invalid
        ("AB1234", False, False, False),  # too short
    ]
    
    all_passed = True
    
    for plate, valid_expected, old_expected, mercosul_expected in tests:
        valid_result = validate_plate(plate)
        old_result = is_old_format_plate(plate)
        mercosul_result = is_mercosul_format_plate(plate)
        
        if (valid_result != valid_expected or 
            old_result != old_expected or 
            mercosul_result != mercosul_expected):
            print(f"  ❌ Plate {plate}: expected valid={valid_expected}, old={old_expected}, mercosul={mercosul_expected}")
            print(f"     got valid={valid_result}, old={old_result}, mercosul={mercosul_result}")
            all_passed = False
        else:
            print(f"  ✅ Plate {plate}: valid={valid_result}, old={old_result}, mercosul={mercosul_result}")
    
    return all_passed


def test_email():
    """Test email validation."""
    print("Testing email validation...")
    
    tests = [
        ("test@example.com", True),
        ("user@domain.com.br", True),
        ("user.name@domain.co.uk", True),
        ("invalid.email", False),
        ("@domain.com", False),
        ("user@", False),
        ("", False),
    ]
    
    all_passed = True
    
    for email, expected in tests:
        result = validate_email(email)
        if result != expected:
            print(f"  ❌ Email {email}: expected {expected}, got {result}")
            all_passed = False
        else:
            print(f"  ✅ Email {email}: {result}")
    
    return all_passed


def test_password():
    """Test password validation."""
    print("Testing password validation...")
    
    # Test length validation
    length_tests = [
        ("12345678", True),   # 8 chars - minimum
        ("1234567", False),   # 7 chars - too short
        ("", False),          # empty
        ("VeryLongPassword123!", True),  # long password
    ]
    
    all_passed = True
    
    for password, expected in length_tests:
        result = validate_password_length(password, 8)
        if result != expected:
            print(f"  ❌ Password length '{password}': expected {expected}, got {result}")
            all_passed = False
        else:
            print(f"  ✅ Password length '{password}': {result}")
    
    # Test strength validation
    strength_tests = [
        ("Password123!", 5),   # Perfect score
        ("password123!", 4),   # Missing uppercase
        ("PASSWORD123!", 4),   # Missing lowercase  
        ("Password!", 4),      # Missing digit
        ("Password123", 4),    # Missing special
        ("12345678", 2),       # Length + digits
        ("weak", 1),           # Only lowercase (no min length)
    ]
    
    for password, expected_score in strength_tests:
        result = validate_password_strength(password)
        if result['score'] != expected_score:
            print(f"  ❌ Password strength '{password}': expected score {expected_score}, got {result['score']}")
            all_passed = False
        else:
            print(f"  ✅ Password strength '{password}': score {result['score']}")
    
    return all_passed


def test_documents():
    """Test CRV and CNH validation."""  
    print("Testing document validation...")
    
    # CRV tests
    crv_tests = [
        ("ABC12345678", True),   # 11 alphanumeric
        ("12345678901", True),   # 11 numeric
        ("ABC123", False),       # too short
        ("", False),             # empty
    ]
    
    all_passed = True
    
    for crv, expected in crv_tests:
        result = validate_crv(crv)
        if result != expected:
            print(f"  ❌ CRV {crv}: expected {expected}, got {result}")
            all_passed = False
        else:
            print(f"  ✅ CRV {crv}: {result}")
    
    # CNH tests
    cnh_tests = [
        ("12345678901", True),    # 11 digits
        ("123.456.789-01", True), # 11 digits with formatting
        ("123456789", False),     # 9 digits - too short
        ("123456789012", False),  # 12 digits - too long
        ("", False),              # empty
    ]
    
    for cnh, expected in cnh_tests:
        result = validate_cnh(cnh)
        if result != expected:
            print(f"  ❌ CNH {cnh}: expected {expected}, got {result}")
            all_passed = False
        else:
            print(f"  ✅ CNH {cnh}: {result}")
    
    return all_passed


def run_all_tests():
    """Run all test suites."""
    print("🧪 Running Brazilian Document Validator Tests")
    print("=" * 60)
    
    test_functions = [
        test_cpf,
        test_phone, 
        test_plates,
        test_email,
        test_password,
        test_documents,
    ]
    
    results = []
    
    for test_func in test_functions:
        try:
            result = test_func()
            results.append(result)
            print()
        except Exception as e:
            print(f"  ❌ Test {test_func.__name__} failed with exception: {e}")
            traceback.print_exc()
            results.append(False)
            print()
    
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed!")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)