# test_transaction.py

import unittest
from product_management.product import Product
from product_management.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        product = Product("Book", 10, "A great book for fundraising")
        transaction = Transaction(product, 2, 20, "Credit Card")
        self.assertEqual(transaction.product, product)
        self.assertEqual(transaction.quantity, 2)
        self.assertEqual(transaction.total_amount, 20)
        self.assertEqual(transaction.payment_method, "Credit Card")

if __name__ == '__main__':
    unittest.main()
