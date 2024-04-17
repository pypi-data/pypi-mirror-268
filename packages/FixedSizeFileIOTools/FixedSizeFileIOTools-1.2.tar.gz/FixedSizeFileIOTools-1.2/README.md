# FixedSizeFileIOTools
Python library for handling fixed sized files (120 characters), with interactive CLI.

## Contents
Library on this Repo consist of **3** main files.

+ > **models.py** - consist of pydantict models for object structures.
    * > Functionalites:
        * > Three seperate models: 
            * Header - Represents a header with specific fields.
             (name, surname, patronymic, address) 
            * Transaction - Represents a transaction with a specific fields. (counter, amount, currency, reserved)
            * Footer - Represents a footer with specific fields.
            (total counter, control sum, reserved)
        * > Methods:
            1. **_get_header()_** - get all fields of header with formated lengths.
            2. **_get_transaction()_**- get all fields of transaction with formated lengths.
            3. **_get_footer()_** - get all fields of footer with formated lengths.
            4. **_get_field()_** - get any field of model.
            5. **_change_field()_** - change field of model.
            6. **_close_field()_** - close field for modification.
            7. **_open_field()_** - open field for modification.
            8. **_is_field_modifiable()_** - check is field modifiable.
            9. **_decimal_places()_** - check if provided amount in transaction has more than 3 decimal places.
            10. **_currency_must_be_from_list()_** - check if provided currency is from predifined list.

+ > **file_handler.py** - Handles fixed-format files containing headers, transactions, and footers.
    * > Functionalites:
        * > Methods:
            1. __init__: Initializes the FixedFileHandler object.
            2. **_validate_file_structure()_**: Validates the structure of the input file.
            3. **_validate_records_structure()_**: Validates the structure of the records stored in the dictonary.
            4. **_read_records()_**: Reads records from the input file and stores them in the records dictionary.
            5. **_write_records()_**: Writes records stored in the object to an output file.
            6. **_add_new_transaction()_**: Adds a new transaction to the records dictionary.
            7. **_add_header()_**: Adds a header record to the records dictionary.
            8. **_list_transactions()_**: Lists all transactions stored in the records dictionary.

+ > **cli.py** - Interactive Command-line interface for handling files with fixed length (120 characters in line) records.

    > This CLI provides commands for reading, writing, modifying records and generating sample files.

    > Usage:
        Use the function **run()** to start the interactive CLI.
    * **Commands**:
        1. **read**: Read records from a file.
        2. **write**: Write records to a file.
        3. **add-header**: Add a header record.
        4. **add-transaction**: Add a transaction record.
        5. **list-transactions**: List current transactions.
        6. **get-field**: Get the value of a specific field from a record.
        7. **change-field**: Change the value of a specific field in a record.
        8. **open-field**: Open a field for modification.
        9. **close-field**: Close a field for modification.
        10. **clear-all**: Clear all current stored information (not from file).
        11. **generate-sample_file**: Generate a sample file with transactions.
        12. **help**: Show available commands.

## Tests
>This library was throughly tested using **pytest** in edge scenarios / cases.

>To run tests just write **_pytest -vv_** in terminal at root directory of this project.

## Distribution
You can install and use this library free at 
>https://pypi.org/project/FixedSizeFileIOTools/


### Author 
**_Patryk Jaworki_**
>**17.04.2024** 
