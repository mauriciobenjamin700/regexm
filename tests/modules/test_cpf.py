from src.cpf import (
    is_cpf_format, format_cpf, validate_cpf
)


def test_is_cpf_format():

    assert is_cpf_format("12345678909") is True
    assert is_cpf_format("123.456.789-09") is True
    assert is_cpf_format("1234567890A") is False
    assert is_cpf_format("1234567890") is False
    assert is_cpf_format("123456789012") is False


def test_format_cpf():

    assert format_cpf("123.456.789-09") == "123.456.789-09"
    assert format_cpf("12345678909") == "123.456.789-09"
    assert format_cpf("123A456B789C09") == "123.456.789-09"


def test_validate_cpf():

    assert validate_cpf("584.492.260-31") is True
    assert validate_cpf("111.444.777-35") is True
    assert validate_cpf("00000000000") is False
    assert validate_cpf("11144477735") is True
