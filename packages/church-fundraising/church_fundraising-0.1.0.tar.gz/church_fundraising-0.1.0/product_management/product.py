# product.py

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}"

    # Getters and setters for product attributes
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

# Example usage
if __name__ == "__main__":
    product = Product("Book", 10, "A great book for fundraising")
    print(product)
    product.set_price(15)
    print(product)
