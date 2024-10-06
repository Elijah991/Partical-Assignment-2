class Product:
    """Represents a product with a name, price, and quantity in stock."""

    def __init__(self, product_name, price, quantity_in_stock):
        """Initializes a new Product object.

        Args:
            product_name: The name of the product.
            price: The price of the product.
            quantity_in_stock: The number of available units of the product.
        """
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        """Displays the product's information to the console."""
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")


class ShoppingCart:
    """Represents a shopping cart containing products."""

    total_carts = 0

    def __init__(self):
        """Initializes a new ShoppingCart object.

        Increments the total number of carts created.
        """
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        """Adds a product to the cart if there are sufficient units in stock.

        Args:
            product: The product to add.
            quantity: The quantity to add.
        """
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"{quantity} {product.product_name} added to your cart.")
        else:
            print("Insufficient stock.")

    def remove_from_cart(self, product):
        """Removes a product from the cart.

        Args:
            product: The product to remove.
        """
        for i in range(len(self.items)):
            if self.items[i][0] == product:
                product.quantity_in_stock += self.items[i][1]
                self.items.pop(i)
                print(f"{product.product_name} removed from your cart.")
                break
        else:
            print("Product not found in your cart.")

    def display_cart(self):
        """Displays the contents of the cart to the console."""
        print("Your Cart:")
        for product, quantity in self.items:
            print(f"- {product.product_name} (Quantity: {quantity})")

    def calculate_total(self):
        """Calculates the total price of the items in the cart.

        Returns:
            The total price.
        """
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total


# Create product objects
product1 = Product("Laptop", 200000, 5)
product2 = Product("Smartphone", 80000, 10)
product3 = Product("Headphones", 5000, 20)

# Create shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add products to carts
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart2.add_to_cart(product2, 3)
cart2.add_to_cart(product3, 5)

# Display cart contents and calculate totals
cart1.display_cart()
print("Total:", cart1.calculate_total())
print()
cart2.display_cart()
print("Total:", cart2.calculate_total())