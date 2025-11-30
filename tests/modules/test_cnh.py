from src.cnh import is_cnh_format, format_cnh, validate_cnh


def test_is_cnh_format():
    assert is_cnh_format("12345678901") is True
    assert is_cnh_format("123.456.789-01") is False
    assert is_cnh_format("1234567890A") is False
    assert is_cnh_format("1234567890") is False
    assert is_cnh_format("123456789012") is False


def test_format_cnh():
    assert format_cnh("12345678901") == "12345678901"
    assert format_cnh("  12345678901  ") == "12345678901"
    assert format_cnh("123.456.789-01") == "12345678901"
    assert format_cnh("123-456.789 01") == "12345678901"


def test_validate_cnh():
    # Valid CNH number
    assert validate_cnh("12345678901") is True
    # Invalid CNH numbers
    assert validate_cnh("12345678902") is False
    # Invalid formats
    assert validate_cnh("123.456.789-01") is False
    # Incorrect lengths
    assert validate_cnh("1234567890A") is False
    # Too short
    assert validate_cnh("1234567890") is False
    # Too long
    assert validate_cnh("123456789012") is False
