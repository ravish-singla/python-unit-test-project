# The url from YouTube for this document
# https://www.youtube.com/watch?v=FUrui0DpK5I

# The url from Github for this source code is below:
# https://github.com/Joshwen7947/Unit-Tests
# https://github.com/Joshwen7947/Unit-Tests/blob/main/testing/src/main.py

# For more learning on how to write those additional test cases,
# follow this url from YouTube:
# https://www.youtube.com/watch?v=1Lfv5tUGsn8


""" This is the test module which will test the main module"""

import sys
import os

""" Linking the sys and os for the path without any issues"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import unittest
from src.main import (
    BankAccount, ZeroAmountError, NegativeAmountError,
    InsufficientFundsError, InvalidInputError
)


### 1 Testing Account Initialization ###
class TestBankAccountInit(unittest.TestCase):

    def setUp(self):
        """Create a fresh BankAccount instance before each test."""
        print("Setting up the TestBankAccountInit test...")
        self.account = BankAccount("Test User", 1000.0)

    # valid account creation
    def test_valid_account_creation(self):
        """Test valid account creation with correct inputs."""
        account = BankAccount("John Doe", 100.0)
        self.assertEqual(account.account_holder, "John Doe")
        self.assertEqual(account.balance, 100.0)

    # test account holder
    def test_account_holder(self):
        self.assertIsNotNone(self.account.account_holder)
        self.assertEqual(self.account.account_holder, "Test User")

    # Check account holder with Number passed
    def test_account_holder_numeric_string(self):
        """Test that a non-string account holder raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount(123, 100.0)
        self.assertEqual(str(context.exception), "Account holder name must be a non-empty string")

    # Check account holder with None passed
    def test_account_holder_none(self):
        """Test that a non-string account holder raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount(None, 100.0)
        self.assertEqual(str(context.exception), "Account holder name must be a non-empty string")

    # Check account holder with a True passed
    def test_account_holder_true(self):
        """Test that a non-string account holder raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount(True, 100.0)
        self.assertEqual(str(context.exception), "Account holder name must be a non-empty string")

    # Check account holder with Empty Spaces passed in String
    def test_account_holder_empty(self):
        """Test that an empty account holder name raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount("   ", 100.0)
        self.assertEqual(str(context.exception), "Account holder name cannot be empty")

    # Check account holder with trailing/leading spaces
    def test_account_holder_with_spaces(self):
        """Test that account holder names with extra spaces are trimmed."""
        account = BankAccount("  Alice  ", 50.0)
        # self.assertEqual(account.account_holder, "Alice")
        self.assertEqual(account.account_holder.strip(), "Alice")


    # Check valid balance passed
    def test_valid_balance(self):
        """Test valid balance assignment."""
        account = BankAccount("Bob Dylan", 200.5)
        self.assertEqual(account.balance, 200.5)

    # Check non-numeric balance passed
    def test_balance_non_numeric(self):
        """Test that a non-numeric balance raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount("Diana Hayden", "one hundred")
        self.assertEqual(str(context.exception), "Balance must be numeric")

    # Check None balance passed
    def test_balance_none(self):
        """Test that a None balance raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount("Diana Hayden", None)
        self.assertEqual(str(context.exception), "Balance must be numeric")


    # Check True balance passed
    def test_balance_true(self):
        """Test that a True balance raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount("Diana Hayden", True)
        self.assertEqual(str(context.exception), "Balance must be numeric")

    # Check False balance passed
    def test_balance_false(self):
        """Test that a False balance raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount("Diana Hayden", False)
        self.assertEqual(str(context.exception), "Balance must be numeric")

    # Check negative balance passed
    def test_balance_negative(self):
        """Test that a negative balance raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            BankAccount("Charlie Chaplin", -50.0)
        self.assertEqual(str(context.exception), "Balance cannot be negative")

    def tearDown(self) -> None:
        """Cleanup after each test (not always needed but useful for closing files/connections)."""
        self.account = None # or assigning the account to None object


### 2️ Testing Deposit Functionality ###
class TestBankAccountDeposit(unittest.TestCase):

    def setUp(self):
        """Runs before each test in this class."""
        print("Setting up the TestBankAccountDeposit test...")
        self.account = BankAccount("Test User", 100.0)

    # test initial deposit
    def test_deposit_initial(self):
        self.assertEqual(self.account.balance, 100.0)
        self.assertTrue(self.account.balance >= 0)

    # test deposit
    def test_deposit_valid_amount(self):
        """Test depositing a valid amount."""
        old_balance = self.account.balance
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150.0)
        self.assertGreater(self.account.balance,old_balance)

    # zero deposit
    def test_deposit_zero(self):
        """Test that depositing zero raises an error."""
        with self.assertRaises(ZeroAmountError) as context:
            self.account.deposit(0)
        self.assertEqual(str(context.exception),"Deposit amount must be greater than Zero")

    # negative deposit
    def test_deposit_negative_amount(self):
        """Test that depositing a negative amount raises an error."""
        with self.assertRaises(NegativeAmountError) as context:
            self.account.deposit(-10)
        self.assertEqual(str(context.exception),"Deposit amount must be positive")

    # Check non-numeric deposit
    def test_deposit_non_numeric(self):
        """Test that a non-numeric deposit raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.deposit("one hundred")
        self.assertEqual(str(context.exception), "Deposit amount must be numeric")

    # Check None deposit
    def test_deposit_none(self):
        """Test that a None deposit raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.deposit(None)
        self.assertEqual(str(context.exception), "Deposit amount must be numeric")

    # Check True deposit
    def test_deposit_true(self):
        """Test that a True deposit raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.deposit(True)
        self.assertEqual(str(context.exception), "Deposit amount must be numeric")

    # Check False deposit
    def test_deposit_false(self):
        """Test that a False deposit raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.deposit(False)
        self.assertEqual(str(context.exception), "Deposit amount must be numeric")

    def tearDown(self) -> None:
        """Cleanup after each test (not always needed but useful for closing files/connections)."""
        self.account = None # or assigning the account to None object


### 3️ Testing Withdraw Functionality ###
class TestBankAccountWithdraw(unittest.TestCase):

    def setUp(self):
        """Runs before each test in this class."""
        print("Setting up the TestBankAccountWithdraw test...")
        self.account = BankAccount("Test User", 100.0)

    # test initial balance before withdraw
    def test_withdraw_initial(self):
        self.assertEqual(self.account.balance, 100.0)
        self.assertTrue(self.account.balance >= 0)

    # valid withdraw
    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount."""
        old_balance = self.account.balance
        self.account.withdraw(40)
        self.assertEqual(self.account.balance, 60.0)
        self.assertLess(self.account.balance,old_balance)


    # insufficient funds
    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than the balance raises an error."""
        with self.assertRaises(InsufficientFundsError) as context:
            self.account.withdraw(200)
        self.assertEqual(str(context.exception),"Insufficient funds")

    # zero withdraw
    def test_withdraw_zero(self):
        """Test that withdrawing zero raises an error."""
        with self.assertRaises(ZeroAmountError) as context:
            self.account.withdraw(0)
        self.assertEqual(str(context.exception),"Withdrawal amount must be greater than Zero")

    # negative withdraw
    def test_withdraw_negative_amount(self):
        """Test that withdrawing a negative amount raises an error."""
        with self.assertRaises(NegativeAmountError) as context:
            self.account.withdraw(-10)
        self.assertEqual(str(context.exception),"Withdrawal amount must be positive")

    # Check non-numeric withdraw
    def test_withdraw_non_numeric(self):
        """Test that a non-numeric withdraw raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.withdraw("one hundred")
        self.assertEqual(str(context.exception), "Withdrawal amount must be numeric")

    # Check None withdraw
    def test_withdraw_none(self):
        """Test that a None withdraw raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.withdraw(None)
        self.assertEqual(str(context.exception), "Withdrawal amount must be numeric")

    # Check True withdraw
    def test_withdraw_true(self):
        """Test that a True withdraw raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.withdraw(True)
        self.assertEqual(str(context.exception), "Withdrawal amount must be numeric")

    # Check False withdraw
    def test_withdraw_false(self):
        """Test that a False withdraw raises an error."""
        with self.assertRaises(InvalidInputError) as context:
            self.account.withdraw(False)
        self.assertEqual(str(context.exception), "Withdrawal amount must be numeric")

    def tearDown(self) -> None:
        """Cleanup after each test (not always needed but useful for closing files/connections)."""
        self.account = None # or assigning the account to None object


### 4 Testing Balance Property ###
class TestBankAccountBalanceProp(unittest.TestCase):

    def setUp(self):
        """Runs before each test in this class."""
        print("Setting up the TestBankAccountBalanceProp test...")
        self.account = BankAccount("Test User", 1000.0)

    # test valid balance property
    def test_balance_property(self):
        self.assertEqual(self.account.balance, 1000.0)
        self.assertTrue(self.account.balance > 0)
        self.assertIsInstance(self.account.balance,float)

    def tearDown(self) -> None:
        """Cleanup after each test (not always needed but useful for closing files/connections)."""
        self.account = None # or assigning the account to None object


### 5 Testing Str Method / Function ###
class TestBankAccountStr(unittest.TestCase):

    def setUp(self):
        """Runs before each test in this class."""
        print("Setting up the TestBankAccountStr test...")
        self.account = BankAccount("Test User", 500.0)

    # test proper return from str function/method
    def test_str(self):
        self.assertEqual(self.account.account_holder, "Test User")
        self.assertEqual(self.account.balance, 500.0)
        self.assertEqual(str(self.account),"Account holder: Test User, Balance: 500.0")


    def tearDown(self) -> None:
        """Cleanup after each test (not always needed but useful for closing files/connections)."""
        self.account = None # or assigning the account to None object


"""
In unittest, the tests in a test suite do not guarantee a specific order of
execution by default. This is intentional to ensure that your tests are
independent (i.e., one test's result shouldn't depend on the execution order
or the result of other tests).


"""
def suite():
    suite = unittest.TestSuite()

    # Manually add test cases in the exact order you want
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBankAccountInit))        # 1st
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBankAccountStr))         # 2nd
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBankAccountBalanceProp)) # 3rd
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBankAccountWithdraw))    # 4th (Runs before deposit)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBankAccountDeposit))     # 5th

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
