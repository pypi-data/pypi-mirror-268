import click
import os
import logging
from .file_handler import FixedFileHandler
from .models import Header, Transaction, Footer
import timeit

class FileHandlerCLI:
    """
    Interactive Command-line interface for handling files with fixed length (120 characters in line) records.

    This CLI provides commands for reading, writing, modifying records and generating sample files.

    Usage:
        Use the function run() to start the interactive CLI.

    Commands:
        read: Read records from a file.
        write: Write records to a file.
        add_header: Add a header record.
        add_transaction: Add a transaction record.
        list_transactions: List current transactions.
        get_field: Get the value of a specific field from a record.
        change_field: Change the value of a specific field in a record.
        open_field: Open a field for modification.
        close_field: Close a field for modification.
        clear_all: Clear all current stored information (not from file).
        generate_sample_file: Generate a sample file with transactions.
        help: Show available commands.
    """
    def __init__(self):
        # Loggers
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logs_folder_path = os.path.join(
            os.path.dirname(__file__), '..', 'logs')

        if not os.path.exists(self.logs_folder_path):
            os.makedirs(self.logs_folder_path)

        self.log_file_path = os.path.join(self.logs_folder_path, 'fileHandlerCli.log')
        file_handler = logging.FileHandler(filename=self.log_file_path, mode="w")
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # Instance of FixedFileHandler
        self.file_handler_instance = FixedFileHandler(model_header=Header, model_transaction=Transaction, model_footer=Footer)
        self.logger.info("FixedFileHandler initialized.")

    def validate_key(self, key):
        """
        Validate if the given key is an integer.

        Args:
            key (str): The key to validate.

        Returns:
            int: The validated key.

        Raises:
            click.BadParameter: If the key is not an integer.
        """
        try:
            return int(key)
        except ValueError:
            raise click.BadParameter("Key must be an integer.")

    def run(self):
        """
        Run the interactive CLI.
        """
        @click.group()
        def cli():
            """
            File Handler CLI.
            """
            pass

        @cli.command()
        @click.argument('file_path')
        def read(file_path):
            """
            Read records from a file.

            Args:
                file_path (str): The path to the file.
            """
            start_time = timeit.default_timer()
            self.file_handler_instance.read_records(file_path=file_path)
            end_time = timeit.default_timer()
            execution_time = end_time - start_time
            print(f"Execution time: {execution_time} seconds")
            return self.file_handler_instance.records

        @cli.command()
        @click.argument('file_path')
        def write(file_path):
            """Write records to a file."""
            try:
                self.file_handler_instance.write_records(filepath=file_path)
            except ValueError as e:
                self.logger.error(f"Error: {e}")

        @cli.command()
        @click.option('--name', prompt='Name', help='Name of the person')
        @click.option('--surname', prompt='Surname', help='Surname of the person')
        @click.option('--patronymic', prompt='Patronymic', help='Patronymic of the person')
        @click.option('--address', prompt='Address', help='Address of the person')
        def add_header(name, surname, patronymic, address):
            """
            Add a header record.

            Args:
                name (str): Name of the person.
                surname (str): Surname of the person.
                patronymic (str): Patronymic of the person.
                address (str): Address of the person.
            """
            try:
                if not all([name.strip(), surname.strip(), patronymic.strip(), address.strip()]):
                    raise ValueError("Error: Inputs cannot be empty or contain only spaces.")
                header = Header(field_id='01', name=name, surname=surname, patronymic=patronymic, address=address)
                self.file_handler_instance.add_header(header)
            except ValueError as e:
                self.logger.error(f"Model validation error for header: {e}")
            return self.file_handler_instance.records

        @cli.command()
        @click.option('--amount', prompt='Amount', help='Transaction amount')
        @click.option('--currency', prompt='Currency', help='Transaction currency')
        def add_transaction(amount, currency):
            """
            Add a transaction to at end.

            Args:
                amount (float): Transaction amount.
                currency (str): Transaction currency.
            """
            try:
                float_amount = float(amount)
                transaction = Transaction(field_id='02', counter="1", amount=float_amount, currency=currency, reserved='')
                start_time = timeit.default_timer()
                self.file_handler_instance.add_new_transaction(transaction)
                end_time = timeit.default_timer()
                execution_time = end_time - start_time
                print(execution_time)
            except ValueError as e:
                self.logger.error(f"Model validation error for transacation: {e}")

        @cli.command()
        def list_transactions(): 
            """List current transactions."""
            self.file_handler_instance.list_transactions()

        @cli.command()
        @click.option('--key', prompt='key', help='Key of listed items')
        @click.option('--field_name', prompt='field_name', help='Which field name you would like to get')
        def get_field(key, field_name):
            """
            Get the value of a specific field from the record based on the key.

            Args:
                key (str): Key of the record.
                field_name (str): Name of the field to retrieve.
            """
            try:
                key = self.validate_key(key)
                if not self.file_handler_instance.records:
                    self.logger.info("No records")
                else:
                    logging.debug(type(key))
                    key = int(key)
                    field_name = str(field_name).lower()
                    record = self.file_handler_instance.records[int(key)]
                    print(record.get_field(field_name))
            except (KeyError, ValueError) as e:
                self.logger.error(f"Error: no record under key: {e}")

        @cli.command()
        @click.option('--key', prompt='key', help='Key of listed items')
        @click.option('--field_name', prompt='field_name', help='Which field name you would like to change')
        @click.option('--new_field_value', prompt='new_field_value', help='New value which will be assigned')
        def change_field(key, field_name, new_field_value):
            """
            Change the value of specific field from the record.

            Args:
                key (str): Key of the record.
                field_name (str): Name of the field to change.
                new_field_value (str): New value to assign to the field.
            """
            try:
                key = self.validate_key(key)
                if not self.file_handler_instance.records:
                    self.logger.info("No records")
                else:
                    logging.debug(type(key))
                    key = int(key)
                    field_name = str(field_name).lower()
                    print(field_name)
                    record = self.file_handler_instance.records[int(key)]
                    if not record.is_field_modifiable(field_name):
                        raise ValueError(f"Field '{field_name}' is not open for modification.")
                    if type(record) == self.file_handler_instance.model_header:
                        print(record.change_field(field_name, new_field_value))
                    elif type(record) == self.file_handler_instance.model_transaction:
                        print(record)
                        if field_name == "amount":
                            new_amount = float(new_field_value)
                            max_control_sum = 1000000000000  # Example limit
                            current_control_sum = sum(record.amount for record in self.file_handler_instance.records.values() if isinstance(record, self.file_handler_instance.model_transaction))
                            if new_amount > max_control_sum - current_control_sum:
                                raise ValueError("New trancation amount exceeds control sum limit")
                            else:
                                previous_value = record.get_field(field_name)
                                difference = float(previous_value) - new_amount
                                footer_key = max(self.file_handler_instance.records.keys())
                                footer = self.file_handler_instance.records.get(footer_key)
                                if record.change_field(field_name, new_field_value) == True:
                                    footer.control_sum -= difference
                        
                        print(record.change_field(field_name, new_field_value))
                    elif type(record) == self.file_handler_instance.model_footer:
                        print(record.change_field(field_name, new_field_value))
            except (KeyError, ValueError) as e:
                self.logger.error(f"Error: {e}")

        @cli.command()
        @click.option('--key', prompt='key', help='Key of listed items')
        @click.option('--field_name', prompt='field_name', help='Which field name you would like to open for modification')
        def open_field(key, field_name):
            """
            Open field for modification.

            Args:
                key (str): Key of the record.
                field_name (str): Name of the field to open for modification.
            """
            try:
                key = self.validate_key(key)
                if not self.file_handler_instance.records:
                    self.logger.info("No records")
                else:
                    logging.debug(type(key))
                    key = int(key)
                    field_name = str(field_name).lower()
                    record = self.file_handler_instance.records[int(key)]
                    print(record.open_field(field_name))
            except (KeyError, ValueError):
                self.logger.error(f"No record found for key: {key}")

        @cli.command()
        @click.option('--key', prompt='key', help='Key of listed items')
        @click.option('--field_name', prompt='field_name', help='Which field name you would like to close for modification')
        def close_field(key, field_name):
            """
            Close field for modification.

            Args:
                key (str): Key of the record.
                field_name (str): Name of the field to close for modification.
            """
            try:
                if not self.file_handler_instance.records:
                    self.logger.info("No records")
                else:
                    logging.debug(type(key))
                    key = int(key)
                    field_name = str(field_name).lower()
                    record = self.file_handler_instance.records[int(key)]
                    print(record.close_field(field_name))
            except (KeyError, ValueError) as e:
                self.logger.error(f"No record found for key: {e}")

        @cli.command()
        def clear_all():
            """Clear all current stored information (not from file)"""
            self.file_handler_instance.records.clear()
            self.logger.info("Clearing sucessfull")
        
        @cli.command()
        @click.option('--path', prompt='path', help='path for generated file')
        @click.option('--amount', prompt='amount', help='starting amount')
        @click.option('--increment', prompt='increment', help='value of increment for each transaction')
        @click.option('--num_transactions', prompt='num_transactions', help='number of transactions')
        def generate_sample_file(path: str, amount: float, increment: float, num_transactions: int):
            """
            Generate sample file.

            Args:
                path (str): The path for the generated file.
                amount (float): The starting amount for transactions.
                increment (float): The value of increment for each transaction.
                num_transactions (int): The number of transactions to generate.
            """
            try:
                field_id = '01'
                name = 'John'
                surname = 'Doe'
                patronymic = 'Kowal'
                address = '123 Main St'

                field_id_tran = '02'
                currency = 'USD'
                reserved = ''

                field_id_footer = '03'

                amount = float(amount)
                increment = float(increment)
                num_transactions = int(num_transactions)


                with open(file=path, mode='w') as file:
                    file.write(f'{field_id:<2}{name:<28}{surname:<30}{patronymic:<30}{address:<30}\n') # Return with spaces if needed)
                    counter = 0
                    total_sum = 0
                    for _ in range(num_transactions):
                        counter += 1  # Increment the counter by one each time
                        amount += increment
                        total_sum += amount
                        counter_padded = str(counter).zfill(6)  # Convert counter to string and pad with zeros
                        amount_padded = f'{amount:.2f}'.replace('.', '').zfill(12)  # Adjust padding for decimal parts
                        file.write(f'{field_id_tran:<2}{counter_padded:<6}{amount_padded:<12}{currency:<3}{reserved:<97}\n')
                    total_counter_padded = str(counter).zfill(6)
                    control_sum = f'{total_sum:.2f}'  # Format control sum with two decimal places
                    control_sum_padded = control_sum.replace('.', '').zfill(12)  # Adjust padding for decimal
                    file.write(f'{field_id_footer:<2}{total_counter_padded:<6}{control_sum_padded:<12}{reserved:<100}\n')
                    self.logger.info("Sample file generated!")
            except Exception as e:
                self.logger.error(f'Error occured in file generating: {e}')

        @cli.command()
        def help():
            """Show available commands."""
            click.echo(cli.get_help(click.get_current_context()))

        def prompt_command():
            """
            Prompt user for commands and execute them interactively.
            """
            while True:
                user_input = input(
                    "Enter command (type 'help' for available commands): ")
                if user_input.lower() == 'exit':
                    break
                if not user_input:
                    continue
                try:
                    ctx = cli.make_context('invoke', user_input.split())
                    cli.invoke(ctx)
                except click.exceptions.NoSuchOption as e:
                    self.logger.error(f"Error: {e}")
                except click.exceptions.UsageError as e:
                    self.logger.error(f"Usage Error: {e}")
        
        prompt_command()
