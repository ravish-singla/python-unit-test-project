# The url from YouTube for this document
# https://www.youtube.com/watch?v=FUrui0DpK5I

# The url from Github for this source code is below:
# https://github.com/Joshwen7947/Unit-Tests
# https://github.com/Joshwen7947/Unit-Tests/blob/main/testing/src/main.py

# For more learning on how to write those additional test cases,
# follow this url from YouTube:
# https://www.youtube.com/watch?v=1Lfv5tUGsn8 

""" This is the main module we want to test"""

import logging

logging.basicConfig(level=logging.INFO)

class BankAccountError(Exception):
    """Base class for exceptions in the bank account module."""
    pass

class NegativeAmountError(BankAccountError):
    """Exception raised for negative amounts.
       Inherits from the BankAccountError class."""
    pass

class InsufficientFundsError(BankAccountError):
    """Exception raised when trying to withdraw more than the balance.
       Inherits from the BankAccountError class."""
    pass

class ZeroAmountError(BankAccountError):
    """Exception raised for zero amounts in deposit or withdrawal.
       Inherits from the BankAccountError class."""
    pass

class InvalidInputError(BankAccountError):
    """Exception raised when entering an invalid input (empty strings or list/array etc. or
       complex number or boolean (True/False), None) for the account holder name.
       Exception raised when trying to enter an invalid input (string or list/array etc. or
       complex number or boolean (True/False), None) for the balance.
       Inherits from the BankAccountError class."""
    pass


"""Represents a bank account with validation on initialization."""
class BankAccount:

    """ In the initializer, we have account_holder (i.e. name) and balance."""
    def __init__(self, account_holder: str, balance: float = 0.0) -> None:

        # Validate account holder name
        # First Check for an Invalid input type
        # Then check for invalid values within a str type
        if not isinstance(account_holder, str):
            raise InvalidInputError("Account holder name must be a non-empty string")

        # Check for invalid values within a str type by stripping empty spaces
        self.account_holder = account_holder.strip()
        if not self.account_holder:
            raise InvalidInputError("Account holder name cannot be empty")

        # Validate balance
        if not isinstance(balance, (int,float)) or isinstance(balance, bool):
            raise InvalidInputError("Balance must be numeric")

        # True or False is not caught in the isinstance (int,float)
        # if balance == True or False:
        #     raise InvalidInputError("Balance must be numeric")
        if balance < 0:
            raise InvalidInputError("Balance cannot be negative")

        """ All validation done. Assign sanitized and validated values"""
        self.account_holder = account_holder
        self._balance = balance

    """ Balance Property, return the balance."""
    @property
    def balance(self) -> float:
        return self._balance
    
    """ Deposit function, to deposit an amount in the account and update balance."""
    def deposit(self, amount: float) -> None:
        # Validate amount
        if not isinstance(amount, (int,float)) or isinstance(amount,bool):
            raise InvalidInputError("Deposit amount must be numeric")

        if amount == 0:
            raise ZeroAmountError("Deposit amount must be greater than Zero")
        if amount < 0:
            raise NegativeAmountError("Deposit amount must be positive")
        self._balance += amount
        logging.info(f"Deposited {amount}. New balance: {self.balance}")

    """ Withdraw function, to withdraw an amount from the account and update balance."""
    def withdraw(self, amount: float) -> None:
        # Validate amount
        if not isinstance(amount, (int,float)) or isinstance(amount,bool):
            raise InvalidInputError("Withdrawal amount must be numeric")

        if amount == 0:
            raise ZeroAmountError("Withdrawal amount must be greater than Zero")
        if amount < 0:
            raise NegativeAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self._balance -= amount
        logging.info(f"Withdrew {amount}. New balance: {self.balance}")

    """ String Representation, returning account holder and balance information."""
    def __str__(self) -> str:
        return f"Account holder: {self.account_holder}, Balance: {self.balance}"


wallet = BankAccount("josh",25000)
wallet.withdraw(500)
# wallet.deposit(0)
# wallet.deposit([2])
# wallet.deposit([])
# wallet.deposit("2")
# wallet.deposit('1')
# Need to be handled
# Done now
# wallet.deposit(True)
# wallet.deposit(False)
# Need to be handled
# Done now
# wallet.withdraw(True)
# wallet.withdraw(False)
# wallet.deposit(100.0,1)




