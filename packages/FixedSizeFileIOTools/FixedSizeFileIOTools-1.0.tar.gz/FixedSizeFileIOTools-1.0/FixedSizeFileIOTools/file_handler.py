import logging
import os
from .models import Header, Transaction, Footer

class FixedFileHandler:
    """
    Handles fixed-format files containing headers, transactions, and footers.

    Attributes:
        model_header (Header): An instance of the Header class.
        model_transaction (Transaction): An instance of the Transaction class.
        model_footer (Footer): An instance of the Footer class.
        logger (Logger): Logger instance for logging messages.
        logs_folder_path (str): Path to the folder where log files are stored.
        log_file_path (str): Path to the log file.
        records (dict): Dictionary to store records read from the file.

    Methods:
        __init__: Initializes the FixedFileHandler object.
        validate_file_structure: Validates the structure of the input file.
        validate_records_structure: Validates the structure of the records stored in the dictonary.
        read_records: Reads records from the input file and stores them in the records dictionary.
        write_records: Writes records stored in the object to an output file.
        add_new_transaction: Adds a new transaction to the records dictionary.
        add_header: Adds a header record to the records dictionary.
        list_transactions: Lists all transactions stored in the records dictionary.
    """

    def __init__(self, model_header: Header, model_transaction: Transaction, model_footer: Footer):
        """
        Initializes the FixedFileHandler object.

        Parameters:
            model_header (Header): An instance of the Header class.
            model_transaction (Transaction): An instance of the Transaction class.
            model_footer (Footer): An instance of the Footer class.
        """
        # Loggers
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Can be changed to debug but produces lots of info :)
        self.logs_folder_path = os.path.join(os.path.dirname(__file__), "..", "logs")

        if not os.path.exists(self.logs_folder_path):
            os.makedirs(self.logs_folder_path)

        self.log_file_path = os.path.join(self.logs_folder_path, "fileHandler.log")
        file_handler = logging.FileHandler(filename=self.log_file_path, mode="w")
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # Models
        self.model_header = model_header
        self.model_transaction = model_transaction
        self.model_footer = model_footer
        self.records = {}

    def validate_file_structure(self, file_path):
        """
        Validates the structure of the input file.

        Parameters:
            file_path (str): Path to the input file.

        Returns:
            bool: True if the file structure is valid, False otherwise.
        """
        try:
            footer_present = False
            header_present = False
            transaction_present = False
            control_sum_amount = 0
            trans_cnt = 0

            with open(file=file_path, mode="r") as file:
                for line in file:
                    self.logger.debug(f"Line len: {len(line)}")
                    if len(line) != 121:  # Because of newline sign
                        raise ValueError(f"Bad amount of characters in line {line, len(line)}")

                    record_type = line[:2]  # first two characters
                    if record_type not in ["01", "02", "03"]:  # Check record type
                        raise ValueError(f"Bad record type {record_type}")

                    if record_type == "01":
                        if header_present:
                            raise ValueError("Second Header present bad format of file!")
                        header_present = True
                        self.logger.debug("First header present")

                    elif record_type == "02":
                        self.logger.debug(line)
                        transaction_counter = int(line[2:8].strip())

                        if transaction_counter != trans_cnt + 1:
                            raise ValueError(f"Bad first transaction counter: {transaction_counter}, should be: {trans_cnt + 1}")

                        if trans_cnt > 20000:
                            raise ValueError(f"Transactions can't exceed {20000}, current value: {trans_cnt}")

                        currency = line[20:23].strip()
                        if currency not in self.model_transaction.validCurrency:
                            raise ValueError(f"{line} Currency is not from valid range: {self.model_transaction.validCurrency}, provided: {currency}")

                        trans_cnt += 1
                        self.logger.debug(f"Transaction counter: {transaction_counter}")
                        amount = (float(line[8:20]) / 100)  # Convert to float and divide by 100 to handle decimals
                        control_sum_amount += amount
                        self.logger.debug(f"Control sum: {control_sum_amount}")
                        transaction_present = True
                        self.logger.debug("Transaction present")

                    elif record_type == "03":
                        if footer_present:
                            raise ValueError(f"{line} Second footer present bad format of file!")
                        total_counter_footer = int(line[2:8].strip().zfill(12))
                        control_sum_footer = (float(line[8:20]) / 100)  # Convert to float and divide by 100 to handle decimals
                        self.logger.debug(f"Before validation: {trans_cnt}")
                        if abs(control_sum_amount - control_sum_footer) > 0.01:
                            raise ValueError(f"Bad control sum in footer: {control_sum_footer}, calculated amount: {control_sum_amount}")

                        elif total_counter_footer > 20000 or trans_cnt > 20000:
                            raise ValueError(f"Bad total counter in footer: {total_counter_footer}, should be: equal or less {20000}")
                        footer_present = True
                        self.logger.debug("First footer present.")
            self.logger.debug(f"header_present: {header_present}, transaction_present: {transaction_present}, footer_present: {footer_present}")
            return header_present and transaction_present and footer_present
        except FileNotFoundError:
            self.logger.error(f"File not found {file_path}")
            return False
        except ValueError as e:
            self.logger.error(f"Error occurred while validating file structure: {e}")
            return False

    def validate_records_structure(self):
        """
        Validates the structure of the records stored in the dictonary.

        Returns:
            bool: True if the records structure is valid, False otherwise.
        """
        header_present = False
        transaction_present = False
        footer_present = False

        print(self.records)

        for key, record in self.records.items():
            if isinstance(record, Header):
                print(record)
                header_present = True
            elif isinstance(record, Transaction):
                print(record)
                transaction_present = True
            elif isinstance(record, Footer):
                print(record)
                footer_present = True
            else:
                logging.info("No valid record found")

        if not (header_present and footer_present and transaction_present):
            raise ValueError("Invalid record structure: Missing header, footer, or transaction(s).")

        # Validate the sequential order of transaction counters
        transaction_counters = [int(record.counter) for key, record in self.records.items()if isinstance(record, Transaction)]
        if transaction_counters != list(range(1, len(transaction_counters) + 1)):
            raise ValueError("Invalid transaction counters: Not sequential starting from 1.")

        # Calculate control sum and compare with the one in the footer
        total_amount = sum(record.amount for key, record in self.records.items() if isinstance(record, Transaction))
        footer = next((record for key, record in self.records.items() if isinstance(record, Footer)),None,)
        if footer is None:
            raise ValueError("Missing footer.")

        if total_amount != footer.control_sum:
            raise ValueError(f"Control sum mismatch: Calculated sum is {total_amount}, but footer specifies {footer.control_sum}.")

        # Check if the total counter in the footer matches the number of transactions
        total_transactions = sum(1 for key, record in self.records.items() if isinstance(record, Transaction))
        logging.info(total_transactions)
        if total_transactions != int(footer.total_counter):
            raise ValueError(f"Total counter mismatch: Total transactions {total_transactions} does not match the total counter in the footer {footer.total_counter}.")

        self.logger.info("Records structure validated successfully.")
        return header_present and transaction_present and footer_present

    def read_records(self, file_path):
        """
        Reads records from the input file and stores them in the records dictionary.

        Parameters:
            file_path (str): Path to the input file.

        Returns:
            dict: Dictionary containing the records read from the file.
        """
        if self.validate_file_structure(file_path) == True:
            try:
                with open(file=file_path, mode="r") as file:
                    self.records.clear()
                    counter_key = 1
                    for line in file:
                        record_type = line[:2]
                        try:
                            match record_type:
                                case "01":
                                    header_data = Header(
                                        field_id=line[0:2].strip(),
                                        name=line[2:30].strip(),
                                        surname=line[30:60].strip(),
                                        patronymic=line[60:90].strip(),
                                        address=line[90:120].strip(),
                                    )
                                    self.records[counter_key] = header_data
                                    counter_key += 1
                                case "02":
                                    transaction_data = Transaction(
                                        field_id=line[0:2].strip(),
                                        counter=line[2:8].strip(),
                                        amount=float(line[8:20])/ 100,  # Because of decimal point
                                        currency=line[20:23].upper().strip(),
                                        reserved=line[23:120].strip(),
                                    )
                                    self.records[counter_key] = transaction_data
                                    counter_key += 1
                                case "03":
                                    footer_data = Footer(
                                        field_id=line[0:2].strip(),
                                        total_counter=line[2:8].strip().zfill(12),
                                        control_sum=float(line[8:20])/100,  # Because of decimal point
                                        reserved=line[20:120].strip(),
                                    )
                                    self.records[counter_key] = footer_data
                                    counter_key += 1
                                case _:
                                    self.logger.warning(f"Unknown record type: {record_type} in line {line}"
                                    )
                        except ValueError as e:
                            self.logger.warning(str(e))
                return self.records
            except FileNotFoundError:
                self.logger.error(f"File not found: {file_path}")
                return False
        else:
            self.logger.error(f"Validation of file {file_path} failed.")
            return False

    def write_records(self, filepath: str):
        """
        Writes records stored in the object to an output file.

        Parameters:
            filepath (str): Path to the output file.
        
        Returns:
            True: if writing sucessfull.
            False: if writing unsucessfull.
        """
        try:
            if self.validate_records_structure():
                with open(filepath, "w") as file:
                    file.seek(0)
                    file.truncate()
                    for key, record in self.records.items():
                        if isinstance(record, Header):
                            file.write(f"{record.get_header()}\n")
                        elif isinstance(record, Transaction):
                            file.write(f"{record.get_transaction()}\n")
                        elif isinstance(record, Footer):
                            file.write(f"{record.get_footer()}\n")
                        else:
                            self.logger.warning("Unknown record type")
                            raise ValueError("Unknown record type")
                    self.logger.info(f"Writing sucessfull under filepath: {filepath}")
                    return True
            else:
                raise ValueError("Validation of records structure failed, aborting write")
        except (FileNotFoundError, ValueError) as e:
            self.logger.error(f"Error occured during writing to file: {e}")
            return False

    def add_new_transaction(self, transaction: Transaction):
        """
        Adds a new transaction to the records dictionary.

        Parameters:
            transaction (Transaction): Transaction object to add.

        Returns:
            dict: Updated records dictionary.
        """
        try:
            #No header
            if 1 not in self.records:
                raise ValueError("Header is missing. Cannot add transaction.")
            
            if transaction.field_id != "02":
                raise ValueError(f"Invalid field ID for header :{transaction.field_id}, should be: '02'")
    
            #No transactions adding first transaction
            elif 1 in self.records and 2 not in self.records:

                #To many decimal places
                if not transaction.decimal_places(transaction.amount):
                    raise ValueError("Transaction not added due to decimal places validation failure.")
               
                # Check control sum
                control_sum = transaction.amount
                if control_sum > 1000000000000:
                    raise ValueError("Control sum with new transaction exceeds the limit of 1000000000000.")

                transaction.counter = str(1).zfill(6) # Because we start from 1 transaction
                self.records[len(self.records) + 1] = transaction # We add transaction
                self.logger.info("Transaction updated.")

                #Now we need to add footer
                footer_data = Footer(
                    field_id="03",
                    total_counter=int(1), #Because we have one transaction
                    control_sum=str(control_sum).zfill(12), #Control sum from one transaction
                    reserved=""
                )

                #We add the footer
                self.records[len(self.records) + 1] = footer_data
                return self.records

            # Header present and transaction present
            elif 1 in self.records and 2 in self.records:

                #To many decimal places
                if not transaction.decimal_places(transaction.amount):
                    raise ValueError("Transaction not added due to decimal places validation failure.")
                
                new_transaction_counter = len([record for record in self.records.values() if isinstance(record, Transaction)]) + 1
                control_sum = sum(record.amount for record in self.records.values() if isinstance(record, Transaction)) + transaction.amount

                if new_transaction_counter > 20000:
                    raise ValueError("Cannot add transaction because it will pass the transaction counter limit {20000}")
                
                if control_sum > 1000000000000:
                    raise ValueError("Control sum with new transaction exceeds the limit of 1000000000000.")
                
                max_key = max(self.records.keys())
                transaction.counter = str(new_transaction_counter).zfill(6)
                self.records.pop(max_key)
                self.records[max_key] = transaction
                self.logger.info("Transaction added.")

                # Update footer
                total_counter = len([record for record in self.records.values() if isinstance(record, Transaction)])
                
                footer_data = Footer(
                    field_id="03",
                    total_counter=total_counter,
                    control_sum=str(control_sum).zfill(12),
                    reserved="",
                )

                self.records[max_key + 1] = footer_data
                self.logger.info("Footer updated.")
                return self.records
        except ValueError as e:
            self.logger.error(f"Error occurred while adding transaction: {e}")
            return False

    def add_header(self, header: Header):
        """
        Adds a header record to the records dictionary.

        Parameters:
            header (Header): Header object to add.

        Returns:
            dict: Updated records dictionary.
        """
        try:
            if header.field_id != "01":
                raise ValueError(f"Invalid field ID for header. {header.field_id}, should be: '01")
            
            if 1 not in self.records and header.field_id == "01":
                self.records[1] = header
                self.logger.info("Header added successfully!")
                return True
            else:
                if 1 in self.records:
                    raise ValueError("A header already exists. Cannot add another header.")
        except ValueError as e:
            self.logger.error(f"Error occured while adding header: {e}")
            return False

    def list_transactions(self):
        """
        Lists all transactions stored in the records dictionary.

        Returns:
            True: if listing sucessfull.
            False: if no records found.
        """
        try:
            if not self.records:
                raise ValueError("No records found")
            else:
                header = self.records.get(1)
                max_key = None  # Default value for max_key

                footer_keys = [key for key, record in self.records.items() if isinstance(record, Footer)]

                if footer_keys:
                    max_key = max(footer_keys)
                    footer = self.records.get(max_key)
                else:
                    footer = None

                transactions = [(key, record) for key, record in self.records.items() if isinstance(record, Transaction)]

                if header:
                    print(f"Key:|{1}| Name: |{header.name}| Surname: |{header.surname}| Patronymic: |{header.patronymic}| Address: |{header.address}|")
                if transactions:
                    for key, transaction in transactions:
                        print(f"Key:|{key}| Counter: |{transaction.counter}| Amount: |{transaction.amount}| Currency: |{transaction.currency.upper()}|")
                if footer:
                    print(f"Key:|{max_key}| Total_counter: |{footer.total_counter}| Control_sum: |{footer.control_sum:.2f}|")
                
                return True 
        except ValueError as e:
            self.logger.error(f"Error occured durring listing transactions {e}")
            return False