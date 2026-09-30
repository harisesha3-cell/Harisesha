class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []
        
    def add_product(self, product):
        self.cart.append(product)
        print(f"Added '{product.name}' to the cart.")
        
    def remove_product(self, product_name):
        for item in self.cart:
            if item.name.lower() == product_name.lower():
                self.cart.remove(item)
                print(f"Removed '{product_name}' from the cart.")
                return
        print(f"Product '{product_name}' not found in cart.")
        
    def calculate_total_price(self):
        return sum(item.price for item in self.cart)
        
    def display_products(self):
        print("\n--- Shopping Cart Summary ---")
        if not self.cart:
            print("Cart is empty.")
        for item in self.cart:
            print(f"- {item.name}: ${item.price}")
        print(f"Total Price: ${self.calculate_total_price()}")

cart = ShoppingCart()

p1 = Product("Laptop", 950)
p2 = Product("Mouse", 30)

cart.add_product(p1)
cart.add_product(p2)
cart.display_products()

cart.remove_product("Mouse")
cart.display_products()
