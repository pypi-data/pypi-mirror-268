# test_product.py

import unittest
from product_management.product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Book", 10, "A great book for fundraising")
        self.assertEqual(product.get_name(), "Book")
        self.assertEqual(product.get_price(), 10)
        self.assertEqual(product.get_description(), "A great book for fundraising")

if __name__ == '__main__':
    unittest.main()
