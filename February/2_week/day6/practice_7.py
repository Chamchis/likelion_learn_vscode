class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        
    def total_price(self):
        return sum(product.price for product in self.products)

cart = ShoppingCart()
cart.add_product(Product("Book",9.99))
cart.add_product(Product("Game",59.99))
print(cart.total_price())