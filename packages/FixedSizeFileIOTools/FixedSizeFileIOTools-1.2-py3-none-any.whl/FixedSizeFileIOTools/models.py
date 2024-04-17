import logging
from typing import ClassVar
from pydantic import BaseModel, Field, field_validator

class Header(BaseModel):
    """
    Represents a header with specific fields.

    Attributes:
        field_id (str): The ID of the header field. Max length is 2 characters.
        name (str): The name associated with the header. Max length is 28 characters.
        surname (str): The surname associated with the header. Max length is 30 characters.
        patronymic (str): The patronymic associated with the header. Max length is 30 characters.
        address (str): The address associated with the header. Max length is 30 characters.
    """

    field_id: str = Field(max_length=2)
    name: str = Field(max_length=28)
    surname: str = Field(max_length=30)
    patronymic: str = Field(max_length=30)
    address: str = Field(max_length=30)

    _ismodifiable = {'field_id': False, 'name': True,
                     'surname': True, 'patronymic': True, 'address': True}
    """Dictonary to track modifiability of status of fields"""

    def __str__(self):
        """Returns a string representation of the header."""
        return f'Header: [field_id={self.field_id}, name={self.name}, surname={self.surname}, patronymic={self.patronymic}, address={self.address}]'

    def get_header(self):
        """
        Get all fields of Header formatted with fixed lengths.

        Returns:
            str: The header fields formatted with fixed lengths.
        """
        return f'{self.field_id:<2}{self.name:<28}{self.surname:<30}{self.patronymic:<30}{self.address:<30}'  # Return with spaces if needed

    def get_field(self, field_name: str):
        """
        Get the value of a specific field.
    
        Parameters:
            field_name (str): The name of the field to retrieve.
    
        Returns:
            Any: The value of the specified field, or False if the field does not exist.
    
        Raises:
            ValueError: If an unexpected error occurs.
        """
        try:
            if field_name in self.model_fields_set:
                return getattr(self, field_name)
            else:
                raise ValueError(f"Field {field_name} does not exist in Header model.")
        except ValueError as e:
            logging.error(f"Value error occured: {e}")
            return False

    def change_field(self, field_name: str, new_value):
        """
        Change the value of a field while keeping others unchanged.

        Parameters:
            field_name (str): The name of the field to change.
            new_value (Any): The new value to assign to the field.

        Returns:
            bool: True if the field was successfully changed, False otherwise.
        """
        try:
            assert self._ismodifiable.get(field_name), f'Field {field_name} is not present or not modifiable.'
            max_len_obj = self.model_fields[field_name].metadata[0]
            max_length = max_len_obj.max_length
            if len(new_value) > max_length:
                raise ValueError(f"New value for {field_name} exceeds maximum length of {max_length}")
            setattr(self, field_name, new_value)
            return True
        except (ValueError, AssertionError) as e:
            logging.error(f"Value error occured: {e}")
            return False

    def close_field(self, field_name: str):
        """
        Close a field for modification.

        Parameters:
            field_name (str): The name of the field to close.

        Returns:
            bool: True if the field was successfully closed, False otherwise.

        Raises:
            AssertionError: if field_name is not present or is not modifiable.
        """
        try:
            assert field_name in self._ismodifiable, f'Field {field_name} is not present.'
            self._ismodifiable[field_name] = False
            return True
        except AssertionError as e:
            logging.error(f"Assertion error occured: {e}")
            return False

    def open_field(self, field_name: str):
        """
        Open a closed field for modification.

        Parameters:
            field_name (str): The name of the field to open.

        Returns:
            bool: True if the field was successfully opened, False otherwise.
        """
        try:
            assert field_name in self._ismodifiable, f'Field {field_name} is not present'
            self._ismodifiable[field_name] = True
            return True
        except AssertionError as e:
            logging.error(f"Assertion error occured: {e}")
            return False

    def is_field_modifiable(self, field_name):
        """
        Check if a field is modifiable.

        Parameters:
            field_name (str): The name of the field to check.

        Returns:
            bool: True if the field is modifiable, False otherwise.
        """
        return self._ismodifiable.get(field_name, False)


class Transaction(BaseModel):
    """
    Represents a transaction with a specific fields.

    Attributes:
        field_id (str): The id of the transaction field. Max length is 2 characters.
        counter (str): The counter of the transaction, starts from 1 then incremented. Max length is 6 characters
        amount (float): The amount of the transaction, value should be greater than 0 and lesser than 1000000000000. Max length 12 characters.
        currency (str): The type of currency that was in transaction. Max length 3 characters.
        reserved (str): The reserved field, filled with spaces to match 120 characters in total
    """
    field_id: str = Field(max_length=2)
    counter: str = Field(max_length=6)
    amount: float = Field(gt=0, le=1000000000000)
    currency: str = Field(max_length=3)
    reserved: str = Field(max_length=97)

    _ismodifiable = {'field_id': False, 'counter': True,
                     'amount': True, 'currency': True, 'reserved': True}
    """Dictonary to track modifiability of status of fields"""

    validCurrency: ClassVar[list[str]] = ['USD', 'GBP', 'JPN', 'EUR', 'CAD', 'AUD']
    """List of strings with valid currencies"""

    @staticmethod
    def decimal_places(amount: float):
        """
        Check decimal places of provided values.

        Parameters:
            amount (float): The amount to check for decimal places.

        Raises:
            ValueError: If the provided amount has more than two decimal places.
        """
        if amount is not None and isinstance(amount, float):
            decimal_part = str(amount).split('.')[1] if '.' in str(amount) else ''
            if len(decimal_part) > 2:
                raise ValueError(f'Amount must have max 2 values in the decimal part, provided: {len(decimal_part)} with: {amount}')
            else:
                return True
        else:
            raise ValueError("Invalid amount")

    @field_validator('currency')
    def currency_must_be_from_list(cls, currency: str):
        """
        Validate that the currency is in the valid currency list.

        Parameters:
            currency (str): The currency to validate.

        Returns:
            str: The validated currency.

        Raises:
            ValueError: If the currency is not in the valid currency list.
        """
        if currency not in cls.validCurrency:
            raise ValueError(f'Must be from currency {cls.validCurrency}')
        return currency.upper()

    def __str__(self):
        """
        Return a string representation of the Transaction object.
        """
        return f'Transaction: [field_id={self.field_id}, counter={self.counter}, amount={self.amount}, currency={self.currency}, reserved={self.reserved}]'

    def get_transaction(self):
        """
        Get all fields of transaction formatted with fixed lengths.

        Returns:
            str: The transaction fields formatted with fixed lengths.
        """
        counter_padded = self.counter.zfill(6)
        amount_padded = f'{self.amount:.2f}'.replace('.', '').zfill(12)  # Adjust padding for decimal parts
        return f'{self.field_id:<2}{counter_padded:<6}{amount_padded:<12}{self.currency.upper():<3}{self.reserved:<97}'

    def get_field(self, field_name: str):
        """
        Get the value of a specific field.

        Parameters:
            field_name (str): The name of the field to retrieve.

        Returns:
            Any: The value of the specified field.

        Raises:
            ValueError: If the specified field does not exist in the Transaction model.
        """
        try:
            if field_name in self.model_fields_set:
                return getattr(self, field_name)
            else:
                raise ValueError(f"Field {field_name} does not exist in Header model.")
        except ValueError as e:
            logging.error(f"Value error occured: {e}")
            return False

    def change_field(self, field_name: str, new_value):
        """
        Change the value of a field while keeping others unchanged.

        Parameters:
            field_name (str): The name of the field to change.
            new_value (Any): The new value to assign to the field.

        Returns:
            bool: True if the field was successfully changed, False otherwise.

        Raises:
            AssertionError: If the specified field is not present or not modifiable.
            ValueError: If the new value is invalid or exceeds the maximum length.
        """
        try:
            assert self._ismodifiable.get(field_name), f'Field {field_name} is not present or not modifiable.'
            if field_name == 'amount':
                gt = int(self.model_fields[field_name].metadata[0].gt)
                lt = int(self.model_fields[field_name].metadata[1].le)
                if float(new_value) > gt and float(new_value) < lt:
                    if self.decimal_places(float(new_value)):
                        setattr(self, field_name, float(new_value))
                        return True
                    else:
                        return False
                else:
                    raise ValueError(f'New value need to be greater than {gt} and lesser than {lt}')
            elif field_name == 'counter':
                setattr(self, field_name, new_value)
                return True
            else:
                max_len_obj = self.model_fields[field_name].metadata[0]
                max_length = max_len_obj.max_length
                if len(new_value) > max_length:
                    raise ValueError(f"New value for {field_name} exceeds maximum length of {max_length}")
                if new_value not in self.validCurrency:
                    raise ValueError(f'Currency not from valid range {self.validCurrency}, provided: {new_value}')
                elif len(new_value) <= max_length:
                    setattr(self, field_name, new_value)
                    return True
        except (AssertionError, ValueError) as e:
            logging.error(f"Error occured: {e}")
            return False

    def close_field(self, field_name: str):
        """
        Close a field for modification.

        Parameters:
            field_name (str): The name of the field to close.

        Returns:
            bool: True if the field was successfully closed, False otherwise.

        Raises:
            AssertionError: If the specified field is not present.
        """
        try:
            assert field_name in self._ismodifiable, f'Field {field_name} is not present'
            self._ismodifiable[field_name] = False
            return True
        except AssertionError as e:
            logging.error(f"Assertion error has occured: {e}")
            return False

    def open_field(self, field_name: str):
        """
        Open a closed field for modification.

        Parameters:
            field_name (str): The name of the field to open.

        Returns:
            bool: True if the field was successfully opened, False otherwise.

        Raises:
            AssertionError: If the specified field is not present.
        """
        try:
            assert field_name in self._ismodifiable, f'Field {field_name} is not present'
            self._ismodifiable[field_name] = True
            return True
        except AssertionError as e:
            logging.error(f"Assertion error has occured: {e}")
            return False

    def is_field_modifiable(self, field_name):
        """
        Check if a field is modifiable.

        Parameters:
            field_name (str): The name of the field to check.

        Returns:
            bool: True if the field is modifiable, False otherwise.
        """
        return self._ismodifiable.get(field_name, False)


class Footer(BaseModel):
    """
    Represents a footer with specific fields.

    Attributes:
        field_id (str): The ID of the header field. Max length is 2 characters.
        total_counter (int): The total number of transactions. Need to be greater than 0 and lesser than 20001. 6 Characters.
        control_sum (float): The control sum from all amount of transactions. Need to be greater than 0 and lesser than 1000000000000.
        reserved (str): The resereved place filled with spaces to match 120 characters. Max length 100.
    """
    field_id: str = Field(max_length=2)
    total_counter: int = Field(gt=0, lt=20001)
    control_sum: float = Field(gt=0, lt=1000000000000)
    reserved: str = Field(max_length=100)

    _ismodifiable = {'field_id': False, 'total_counter': True, 
                     'control_sum': True, 'reserved': True}
    """Dictonary to track modifiability of status of fields"""

    @staticmethod
    def decimal_places(control_sum: float):
        """
        Check decimal places of provided values.

        Parameters:
            control_sum (float): The amount to check for decimal places.

        Raises:
            ValueError: If the provided amount has more than two decimal places.
        """
        if control_sum is not None and isinstance(control_sum, float):
            decimal_part = str(control_sum).split('.')[1] if '.' in str(control_sum) else ''
            if len(decimal_part) > 2:
                raise ValueError(f'Amount must have max 2 values in the decimal part, provided: {len(decimal_part)} with: {control_sum}')
            else:
                return True
        else:
            raise ValueError("Invalid amount")

    def __str__(self):
        return f'Footer: [field_id={self.field_id}, total_counter={self.total_counter}, control_sum={self.control_sum}, reserved={self.reserved}]'

    def get_footer(self):
        """
        Get all fields of the footer.

        Returns:
            str: The footer fields formatted with fixed lengths.
        """
        total_counter_padded = str(self.total_counter).zfill(6)
        control_sum_padded = f'{self.control_sum:.2f}'.replace('.', '').zfill(12)  # Adjust padding for decimal parts
        logging.debug(control_sum_padded)
        return f'{self.field_id:<2}{total_counter_padded:<6}{control_sum_padded:<12}{self.reserved:<100}'

    def get_field(self, field_name: str):
        """
        Get the value of a specific field.

        Parameters:
            field_name (str): The name of the field to retrieve.

        Returns:
            Any: The value of the specified field.

        Raises:
            ValueError: If the specified field does not exist in the Footer model.
        """
        try:
            if field_name in self.model_fields_set:
                return getattr(self, field_name)
            else:
                raise ValueError(f"Field {field_name} does not exist in Header model.")
        except ValueError as e:
            logging.error(f"Value error occured: {e}")
            return False

    def change_field(self, field_name: str, new_value):
        """
        Change the value of a field while keeping others unchanged.

        Parameters:
            field_name (str): The name of the field to change.
            new_value (Any): The new value to assign to the field.

        Returns:
            bool: True if the field was successfully changed, False otherwise.

        Raises:
            AssertionError: If the specified field is not present or not modifiable.
            ValueError: If the new value is invalid or exceeds the maximum length.
        """
        try:
            assert self._ismodifiable.get(field_name), f'Field {field_name} is not present or not modifiable.'
            if field_name == 'total_counter':
                gt = int(self.model_fields[field_name].metadata[0].gt)
                lt = int(self.model_fields[field_name].metadata[1].lt)
                if int(new_value) > gt and int(new_value) < lt:
                    setattr(self, field_name, int(new_value))
                    return True
                else:
                    raise ValueError(f'New value need to be greater than {gt} and lesser than {lt}')
            elif field_name == 'control_sum':
                gt = int(self.model_fields[field_name].metadata[0].gt)
                lt = int(self.model_fields[field_name].metadata[1].lt)
                if float(new_value) > gt and float(new_value) < lt:
                    if not self.decimal_places(float(new_value)):
                        setattr(self, field_name, float(new_value))
                        return True
                else:
                    raise ValueError(f'New value need to be greater than {gt} and lesser than {lt}')
            else:
                max_len_obj = self.model_fields[field_name].metadata[0]
                max_length = max_len_obj.max_length

                if len(new_value) > max_length:
                    raise ValueError(f"New value for {field_name} exceeds maximum length of {max_length}")
                setattr(self, field_name, new_value)
                return True
        except (ValueError, AssertionError) as e:
            logging.error(f"Error occured {e}")
            return False

    def close_field(self, field_name: str):
        """
        Close a field for modification.

        Parameters:
            field_name (str): The name of the field to close.

        Returns:
            bool: True if the field was successfully closed, False otherwise.

        Raises:
            AssertionError: If the specified field is not present.
        """
        try:
            assert field_name in self._ismodifiable, f'Field {field_name} is not present'
            self._ismodifiable[field_name] = False
            return True
        except AssertionError as e:
            logging.error(f"Assertion error occured: {e}")
            return False

    def open_field(self, field_name: str):
        """
        Open a closed field for modification.

        Parameters:
            field_name (str): The name of the field to open.

        Returns:
            bool: True if the field was successfully opened, False otherwise.

        Raises:
            AssertionError: If the specified field is not present.
        """
        try:
            assert field_name in self._ismodifiable, f'Field {field_name} is not present'
            self._ismodifiable[field_name] = True
            return True
        except AssertionError as e:
            logging.error(f"Assertion error occured {e}")
            return False

    def is_field_modifiable(self, field_name):
        """
        Check if a field is modifiable.

        Parameters:
            field_name (str): The name of the field to check.

        Returns:
            bool: True if the field is modifiable, False otherwise.
        """
        return self._ismodifiable.get(field_name, False)