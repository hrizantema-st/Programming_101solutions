import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount("Rado", 100, "$")

    def test_create_new_account_instance(self):
#       self.assertTrue(isinstance(self.my_account, BankAccount))
        self.assertEqual(self.my_account.name, "Rado")
        self.assertEqual(self.my_account.balance, 100)
        self.assertEqual(self.my_account.currency, "$")


    def test_int_cast(self):
        self.assertEqual(int(self.my_account), 100)

    def test_str_cast(self):
        helper_str = "Bank account for Rado with balance of 100$"
        self.assertEqual(str(self.my_account), helper_str)

    def testing_the_current_balance(self):
        self.assertEqual(100, self.my_account.get_balance())

    def test_deposit_amount(self):
        self.my_account.deposit(1000)
        self.assertEqual(1100, self.my_account.balance)

    def test_deposit_with_negative_amount(self):
        with self.assertRaises(ValueError):
            self.my_account.deposit(-110)

        self.assertEqual(self.my_account.balance, 100)

    def test_withdraw_amount(self):
        self.assertTrue(self.my_account.withdraw(0))

    def test_value_error_raises_from_greater_amount(self):
        self.assertFalse(self.my_account.withdraw(110))

    def test_value_error_raises_from_negative_balance(self):
        with self.assertRaises(ValueError):
            current_account = BankAccount("Ivo", -10, "$")

    def test_type_error_raises_from_float_balance(self):
        with self.assertRaises(TypeError):
            current_account = BankAccount("Az", 0.25, "$")

    def test_transfer_to_different_currency(self):
        your_account = BankAccount("Ivo", 200, "&")

        with self.assertRaises(ValueError):
            self.my_account.transfer_to(your_account, 200)

        self.assertEqual(self.my_account.balance, 1000)
        self.assertEqual(your_account.balance, 200)

    def test_transfert_more_money_than_we_have(self):
        your_account = BankAccount("Ivo", 200, "$")

        self.assertFalse(your_account.transfer_to(self.my_account, 300))
        self.assertEqual(self.my_account.balance, 1000)
        self.assertEqual(your_account.balance, 200)

    def test_tranfer_to(self):
        your_account = BankAccount("Ivo", 200, "$")
        self.assertTrue(self.my_account.transfer_to(your_account, 50))
        self.assertEqual(your_account.balance, 250)
        self.assertEqual(my_account.balance, 50)

if __name__ == '__main__':
    unittest.main()
