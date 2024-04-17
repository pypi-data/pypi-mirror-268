import sys  
sys.path.append('FixedSizeFileIOTools')

import os
import pytest
from pydantic import ValidationError
from FixedSizeFileIOTools.models import Header, Transaction, Footer
from FixedSizeFileIOTools.file_handler import FixedFileHandler

@pytest.fixture
def model_header():
    return Header(field_id="01", name="John", surname="Doe", patronymic="Smith", address="123 Main St")

@pytest.fixture
def model_transaction():
    return Transaction(field_id="02", counter="000001", amount=1231, currency="USD", reserved="")

@pytest.fixture
def model_footer():
    return Footer(field_id="03", total_counter="000001", control_sum=1231.12, reserved=" ")

@pytest.fixture
def file_handler(model_header, model_transaction, model_footer):
    return FixedFileHandler(model_header, model_transaction, model_footer)


def test_validate_file_structure(file_handler):
    file_path_1 = "test_file_1.txt"
    file_path_2 = "test_file_2.txt"
    file_path_3 = "test_file_3.txt"
    file_path_4 = "test_file_4.txt"
    file_path_5 = "test_file_5.txt"
    file_path_6 = "test_file_6.txt"
    file_path_7 = "test_file_7.txt"
    file_path_8 = "test_file_8.txt"

    #Valid file
    with open(file_path_1, "w") as file:
        file.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file.write("02000001000000123112USD                                                                                                 \n")
        file.write("03000001000000123112                                                                                                    \n")

    #Bad line lenght
    with open(file_path_2, 'w') as file2:
        file2.write("012John                        Doe                           Smith                         123 Main St                   \n")
        file2.write("02000001000000123112USDeeeee                                                                                                 \n")
        file2.write("03000001000000123112eeeeeeee                                                                                                    \n")

    #Bad first transaction counter
    with open(file_path_3, "w") as file3:
        file3.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file3.write("02000002000000123112USD                                                                                                 \n")
        file3.write("03000001000000123112                                                                                                    \n")

    #Bad control sum
    with open(file_path_4, "w") as file4:
        file4.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file4.write("02000001000000123112USD                                                                                                 \n")
        file4.write("03000001000000123110                                                                                                    \n")

    #Bad record type
    with open(file_path_5, "w") as file5:
        file5.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file5.write("02000001000000123112USD                                                                                                 \n")
        file5.write("04000001000000123112USD                                                                                                 \n")
        file5.write("03000001000000123110                                                                                                    \n")

    #Bad currency type
    with open(file_path_6, "w") as file6:
        file6.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file6.write("02000001000000123112USD                                                                                                 \n")
        file6.write("02000002000000123112XYZ                                                                                                 \n")
        file6.write("03000002000000123110                                                                                                    \n")
    
    # Two footers
    with open(file_path_7, "w") as file7:
        file7.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file7.write("02000001000000123112USD                                                                                                 \n")
        file7.write("02000002000000123112XYZ                                                                                                 \n")
        file7.write("03000002000000123110                                                                                                    \n")
        file7.write("03000002000000123110                                                                                                    \n")
    
    # Two headers
    with open(file_path_8, "w") as file8:
        file8.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file8.write("01John                        Doe                           Smith                         123 Main St                   \n")
        file8.write("02000001000000123112USD                                                                                                 \n")
        file8.write("02000002000000123112XYZ                                                                                                 \n")
        file8.write("03000002000000123110                                                                                                    \n")

    assert file_handler.validate_file_structure(file_path=file_path_1) is True
    assert file_handler.validate_file_structure(file_path=file_path_2) is False
    assert file_handler.validate_file_structure(file_path=file_path_3) is False
    assert file_handler.validate_file_structure(file_path=file_path_4) is False
    assert file_handler.validate_file_structure(file_path=file_path_5) is False
    assert file_handler.validate_file_structure(file_path=file_path_6) is False
    assert file_handler.validate_file_structure(file_path=file_path_7) is False
    assert file_handler.validate_file_structure(file_path=file_path_8) is False


    os.remove(file_path_1)
    os.remove(file_path_2)
    os.remove(file_path_3)
    os.remove(file_path_4)
    os.remove(file_path_5)
    os.remove(file_path_6)
    os.remove(file_path_7)
    os.remove(file_path_8)

def test_read_records(file_handler):
     assert file_handler.read_records("tests/sample_files/sample_good_file.txt") == file_handler.records
     assert file_handler.read_records("tests/sample_files/sample_bad_file.txt") is False

def test_add_two_headers(file_handler, model_header):
    file_handler.add_header(model_header)
    assert file_handler.add_header(model_header) is False

def test_add_one_header(file_handler, model_header):
    assert file_handler.add_header(model_header) is True

def test_list_transactions():
    new_file_handler = FixedFileHandler(model_header=Header, model_transaction=Transaction, model_footer=Footer)
    header = Header(field_id="01", name="John", surname="Doe", patronymic="Smith", address="123 Main St")
    transaction1 = Transaction(field_id="02", counter="000001", amount=1231, currency="USD", reserved="")
    transaction2 = Transaction(field_id="02", counter="000002", amount=1231.99, currency="USD", reserved="")
    new_file_handler.add_header(header=header)
    new_file_handler.add_new_transaction(transaction=transaction1)
    new_file_handler.add_new_transaction(transaction=transaction2)
    assert new_file_handler.list_transactions() == True

def test_list_empty_transactions():
    new_file_handler = FixedFileHandler(model_header=Header, model_transaction=Transaction, model_footer=Footer)
    assert new_file_handler.list_transactions() is False

def test_add_new_transaction_with_missing_header(file_handler, model_transaction):
    assert file_handler.add_new_transaction(model_transaction) is False

def test_add_transaction_with_bad_decimals(file_handler, model_header): 
    invalid_transacation = Transaction(field_id="02", counter="000001", amount=12.323123213, currency="USD", reserved="")
    file_handler.add_header(model_header)
    assert file_handler.add_new_transaction(invalid_transacation) is False

def test_add_transaction_with_large_amount(file_handler, model_header): 
    file_handler.add_header(model_header)
    with pytest.raises(ValidationError):
        invalid_transacation = Transaction(field_id="02", counter="000001", amount=10000000000000000000, currency="USD", reserved="")
        file_handler.add_new_transaction(invalid_transacation)

def test_amount_exceeds_control_sum(file_handler, model_header):
    file_handler.add_header(model_header)
    valid_transacation = Transaction(field_id="02", counter="000001", amount=999999999999, currency="USD", reserved="")
    invalid_transacation = Transaction(field_id="02", counter="000002", amount=99999, currency="USD", reserved="")
    file_handler.add_new_transaction(valid_transacation)
    assert file_handler.add_new_transaction(invalid_transacation) is False

def test_add_transaction_that_exceed_counter(file_handler, model_transaction):
    file_handler.read_records("tests/sample_full_file.txt")
    assert file_handler.add_new_transaction(model_transaction) is False

def test_add_tranactions_with_bad_currency(file_handler, model_header):
    file_handler.add_header(model_header)
    with pytest.raises(ValidationError):
        invalid_transacation = Transaction(field_id="02", counter="000002", amount=99999, currency="RUB", reserved="")
        file_handler.add_new_transaction(invalid_transacation)

def test_add_header_then_transaction(file_handler, model_header, model_transaction):
     file_handler.add_header(model_header)
     assert file_handler.add_new_transaction(model_transaction) == file_handler.records