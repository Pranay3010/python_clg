# Multi-Tiered "E-Commerce" Backend
# Simulate the logic behind a site like Amazon.
#     --> Classes: Product, ShoppingCart, Order, and PaymentProcessor.
#     --> Polymorphism: Different payment methods (CreditCard, PayPal, Crypto). All have a process_payment() method, but the internal logic for each is totally different.
#     --> Composition: A ShoppingCart isn't a Product, but it contains a list of Product objects.
#     --> Logic: A discount engine that applies Coupon objects to the total price.


class Product:
    def __init__(self,product_id,name,price,stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price=price
        self.stock_quantity = stock_quantity
        
    
    def __str__(self):
        return f"{self.name} (₹{self.price}) | Stock: {self.stock_quantity}"
    
class ShoppingCart:
    def __init__(self):
        self.items = {}   # {product: quantity}

    def addItem(self, product, quantity=1):
        if product.stock_quantity < quantity:
            print(f"Not enough stock for {product.name}")
            return

        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

        product.stock_quantity -= quantity
        print(f"{quantity} x {product.name} added to cart")

    def removeItem(self, product):
        if product in self.items:
            quantity = self.items[product]
            product.stock_quantity += quantity  # restore stock
            del self.items[product]
            print(f"{product.name} removed from cart")
        else:
            print("Product not in cart")

    def getTotalPrice(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def showCart(self):
        if not self.items:
            print("Cart is empty")
            return

        print("\nCart Items:")
        for product, quantity in self.items.items():
            print(f"{product.name} x {quantity} = ₹{product.price * quantity}")

        print(f"Total: ₹{self.getTotalPrice()}")


class Order:
    def __init__(self):
        pass

class PaymentProcessor:
    def __init__(self):
        pass

class CreditCard(PaymentProcessor):

    pass

class Paypal(PaymentProcessor):

    pass

class Crypto(PaymentProcessor):

    pass


class Coupon :
    def __init__(self):
        pass

class Flap_Coupon(Coupon):

    pass

class Percentage_Coupon(Coupon):

    pass


p1 =Product(1,"ONE PLUS",20000,10)
print(p1.__str__())

cart =ShoppingCart()

cart.addItem(p1,2)

cart.showCart()