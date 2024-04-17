import sys
sys.path.append('FixedSizeFileIOTools')

import pytest
from pydantic import ValidationError
from FixedSizeFileIOTools.models import Header, Transaction, Footer

@pytest.fixture
def header_instance():
    return Header(field_id="01", name="John", surname="Doe", patronymic="Smith", address="123 Main St")

def test_header_model_validation():
    valid_header = Header(
        field_id="01",
        name="John",
        surname="Doe",
        patronymic="Smith",
        address="123 Main St"
    )
    assert valid_header.model_validate(valid_header) == valid_header  # Validation should pass

    with pytest.raises(ValidationError):
        invalid_header = Header(
            field_id="01",
            name="John" * 10,  # Exceeds maximum length
            surname="Doe",
            patronymic="Smith",
            address="123 Main St"
        )
        invalid_header.model_validate(invalid_header)

def test_header_str_method(header_instance):
    assert str(header_instance) == "Header: [field_id=01, name=John, surname=Doe, patronymic=Smith, address=123 Main St]"

def test_get_header(header_instance):
    assert header_instance.get_header() == "01John                        Doe                           Smith                         123 Main St                   "

def test_header_get_field(header_instance):
    assert header_instance.get_field(field_name="surname") == "Doe"
    assert header_instance.get_field(field_name="TestTeest") is False

def test_header_change_field(header_instance):
    assert header_instance.change_field(field_name="name", new_value="Marek") is True
    assert header_instance.change_field(field_name="Testtset", new_value="Marek") is False
    assert header_instance.change_field(field_name="name", new_value="agsdgjhasjdhgahjdgsajghdjhgasgjhdasjghdgjhashjgdajhgsdhjgasdjghajhgsddjahgs") is False

def test_header_close_field(header_instance):
    assert header_instance.close_field(field_name="name") is True
    assert header_instance.close_field(field_name="GHAJDgjhdasghjaghj") is False

def test_header_open_field(header_instance):
    assert header_instance.open_field(field_name="surname") is True
    assert header_instance.open_field(field_name="sahjdhagjsgshjdgjhads") is False

def test_header_is_field_modifiable(header_instance):
    assert header_instance.is_field_modifiable(field_name="surname") is True
    assert header_instance.is_field_modifiable(field_name="field_id") is False

@pytest.fixture
def transaction_instance():
    return Transaction(field_id="02", counter="1", amount=1231.12, currency="USD", reserved="")

def test_transaction_validation():
    valid_transaction = Transaction(
        field_id="02",
        counter="1",
        amount=12321.99,
        currency="USD",
        reserved=""
    )
    assert valid_transaction.model_validate(valid_transaction) == valid_transaction

    with pytest.raises(ValidationError):
        invalid_transaction = Transaction(
            field_id="21312312",
            counter="13213123123123123",
            amount=231231.213123,
            currency="RUB",
            reserved=""
        )
        invalid_transaction.model_validate(invalid_transaction)

def test_transaction_decimal_places(transaction_instance):
    invalid_amount = 1312.3213123
    with pytest.raises(ValueError):
        transaction_instance.decimal_places(invalid_amount)

    valid_amount = 12.22
    assert transaction_instance.decimal_places(valid_amount) is True

def test_currency_must_be_from_list(transaction_instance):
    invalid_currency = "RUB"
    with pytest.raises(ValueError):
        transaction_instance.currency_must_be_from_list(invalid_currency)

    valid_currency = "USD"
    transaction_instance.currency_must_be_from_list(valid_currency)

def test_transaction_str_method(transaction_instance):
    assert str(transaction_instance) == "Transaction: [field_id=02, counter=1, amount=1231.12, currency=USD, reserved=]"

def test_get_transaction(transaction_instance):
     assert transaction_instance.get_transaction() == "02000001000000123112USD                                                                                                 "

def test_transaction_get_field(transaction_instance):
    assert transaction_instance.get_field("counter") == "1"
    assert transaction_instance.get_field("ajkhsdghasghdasjh") is False

# def test_transaction_change_field(transaction_instance):
#     with pytest.raises(ValueError):
#         transaction_instance.change_field("amount", 123.122)

def test_transaction_close_field(transaction_instance):
    assert transaction_instance.close_field("amount") is True
    assert transaction_instance.close_field("adsdasdasd") is False

def test_transaction_open_field(transaction_instance):
    assert transaction_instance.open_field(field_name="amount") is True
    assert transaction_instance.open_field(field_name="adhjgsahdghjs") is False

def test_transaction_is_field_modifiable(transaction_instance):
    assert transaction_instance.is_field_modifiable(field_name="field_id") is False
    assert transaction_instance.is_field_modifiable(field_name="amount") is True

@pytest.fixture
def footer_instance():
    return Footer(field_id="03", total_counter=1, control_sum=100.20, reserved="")

def test_footer_model_validation():
    valid_footer = Footer(
        field_id="03",
        total_counter=1,
        control_sum=100.20,
        reserved="",
    )
    assert valid_footer.model_validate(valid_footer) == valid_footer  # Validation should pass

    with pytest.raises(ValidationError):
        invalid_footer = Footer(
            field_id="03",
            total_counter=136216837216783867,
            control_sum=100.207386743867213678,
            reserved="",
            )
        invalid_footer.model_validate(invalid_footer)

def test_footer_decimal_places(footer_instance):
    invalid_amount = 1312.3213123
    with pytest.raises(ValueError):
        footer_instance.decimal_places(control_sum=invalid_amount)

def test_footer_str_method(footer_instance):
    assert str(footer_instance) == "Footer: [field_id=03, total_counter=1, control_sum=100.2, reserved=]"

def test_get_footer(footer_instance):
    assert footer_instance.get_footer() == "03000001000000010020                                                                                                    "
def test_footer_get_field(footer_instance):
    assert footer_instance.get_field(field_name="total_counter") == 1
    assert footer_instance.get_field(field_name="TestTeest") is False

# def test_footer_change_field(footer_instance):
#     assert footer_instance.change_field(field_name="control_sum", new_value=123) is True
#     assert footer_instance.change_field(field_name="total_counter", new_value=2) is True

def test_footer_close_field(footer_instance):
    assert footer_instance.close_field(field_name="control_sum") is True
    assert footer_instance.close_field(field_name="GHAJDgjhdasghjaghj") is False

def test_footer_open_field(footer_instance):
    assert footer_instance.open_field(field_name="total_counter") is True
    assert footer_instance.open_field(field_name="sahjdhagjsgshjdgjhads") is False

def test_footer_is_field_modifiable(footer_instance):
    assert footer_instance.is_field_modifiable(field_name="total_counter") is True
    assert footer_instance.is_field_modifiable(field_name="field_id") is False