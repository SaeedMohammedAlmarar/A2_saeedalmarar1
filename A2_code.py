# EbookStore Class
class EbookStore:
    """
    Represents an e-book store that manages e-books and store details.
    """

    def __init__(self, phone_number: int, address: str, name: str):
        self.ebooks = []  # List of e-books in the store
        self.phone_number = phone_number
        self.address = address
        self.name = name

    # Setters and Getters
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Methods
    def add_ebook(self, ebook):
        self.ebooks.append(ebook)

    def remove_ebook(self, ebook):
        self.ebooks.remove(ebook)

    def display_store(self):
        print(f"Store Name: {self.name}, Address: {self.address}")
        print("Available Ebooks:")
        for ebook in self.ebooks:
            ebook.display_ebook()


# Ebook Class
class Ebook:
    """
    Represents an e-book with details such as title, author, price, genre, and availability.
    """

    def __init__(self, title: str, author: str, price: float, genre: str, availability: str):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.availability = availability

    # Setters and Getters
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_availability(self, availability):
        self.availability = availability

    def get_availability(self):
        return self.availability

    def display_ebook(self):
        print(f"Ebook: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Genre: {self.genre}, Availability: {self.availability}")


# ShoppingCart Class
class ShoppingCart:
    """
    Represents a shopping cart containing e-books for purchase.
    """

    def __init__(self):
        self.items = []  # List of e-books in the cart
        self.total_amount = 0.0  # Total price of items in the cart

    # Setters and Getters
    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount

    def get_total_amount(self):
        return self.total_amount

    # Methods
    def add_item(self, ebook):
        self.items.append(ebook)
        self.total_amount += ebook.price

    def remove_item(self, ebook):
        self.items.remove(ebook)
        self.total_amount -= ebook.price

    def get_item_count(self):
        return len(self.items)

    def display_cart(self):
        print("Shopping Cart:")
        for ebook in self.items:
            ebook.display_ebook()
        print(f"Total Amount (before discounts): ${self.total_amount:.2f}")


# Discount Class
class Discount:
    """
    Represents a generic discount applied to purchases.
    """

    def __init__(self, discount_percentage: float, start_date: str, end_date: str):
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    # Setters and Getters
    def set_discount_percentage(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def get_discount_percentage(self):
        return self.discount_percentage

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_start_date(self):
        return self.start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_end_date(self):
        return self.end_date

    def apply_discount(self, amount):
        return amount * (1 - self.discount_percentage / 100)


# BulkDiscount Class
class BulkDiscount(Discount):
    """
    Represents a discount for bulk purchases.
    """

    def __init__(self, discount_percentage: float, start_date: str, end_date: str, min_items: int):
        super().__init__(discount_percentage, start_date, end_date)
        self.min_items = min_items  # Minimum number of items required for the discount

    def set_min_items(self, min_items):
        self.min_items = min_items

    def get_min_items(self):
        return self.min_items

    def apply_discount(self, cart: ShoppingCart):
        if cart.get_item_count() >= self.min_items:
            return cart.total_amount * (1 - self.discount_percentage / 100)
        return cart.total_amount


# OldCustomerDiscount Class
class OldCustomerDiscount(Discount):
    """
    Represents a discount for loyal customers with a minimum membership duration.
    """

    def __init__(self, discount_percentage: float, start_date: str, end_date: str, min_membership_duration: int):
        super().__init__(discount_percentage, start_date, end_date)
        self.min_membership_duration = min_membership_duration

    def set_min_membership_duration(self, min_membership_duration):
        self.min_membership_duration = min_membership_duration

    def get_min_membership_duration(self):
        return self.min_membership_duration


# Order Class
class Order:
    """
    Represents a customer's order, including discounts, subtotal, and VAT.
    """
    VAT_RATE = 0.08  # VAT percentage (8%)

    def __init__(self, order_id: int, status: str, shopping_cart: ShoppingCart, customer_discount: Discount):
        self.order_id = order_id
        self.status = status
        self.shopping_cart = shopping_cart
        self.customer_discount = customer_discount

    # Setters and Getters
    def set_order_id(self, order_id):
        self.order_id = order_id

    def get_order_id(self):
        return self.order_id

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_shopping_cart(self, shopping_cart):
        self.shopping_cart = shopping_cart

    def get_shopping_cart(self):
        return self.shopping_cart

    def set_customer_discount(self, customer_discount):
        self.customer_discount = customer_discount

    def get_customer_discount(self):
        return self.customer_discount

    # Methods
    def calculate_subtotal(self):
        return self.shopping_cart.total_amount

    def calculate_discounts(self):
        subtotal = self.calculate_subtotal()
        return self.customer_discount.apply_discount(subtotal)

    def calculate_total_with_vat(self):
        discounted_total = self.calculate_discounts()
        return discounted_total * (1 + Order.VAT_RATE)

    def display_order(self):
        print(f"Order ID: {self.order_id}, Status: {self.status}")
        self.shopping_cart.display_cart()
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        print(f"Discounted Total: ${self.calculate_discounts():.2f}")
        print(f"VAT (8%): ${(self.calculate_total_with_vat() - self.calculate_discounts()):.2f}")
        print(f"Final Total (with VAT): ${self.calculate_total_with_vat():.2f}")


# Customer Class
class Customer:
    """
    Represents a customer with details such as name, phone number, account balance, and their orders.
    """

    def __init__(self, name: str, phone_number: int, account_balance: float):
        self.name = name
        self.phone_number = phone_number
        self.account_balance = account_balance
        self.orders = []  # List of orders placed by the customer

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_phone_number(self, phone_number: int):
        self.phone_number = phone_number

    def get_phone_number(self) -> int:
        return self.phone_number

    def set_account_balance(self, account_balance: float):
        self.account_balance = account_balance

    def get_account_balance(self) -> float:
        return self.account_balance

    def place_order(self, order):
        total_with_vat = order.calculate_total_with_vat()
        if self.account_balance >= total_with_vat:
            self.orders.append(order)
            self.account_balance -= total_with_vat
            print(f"Order placed successfully! Remaining balance: ${self.account_balance:.2f}")
        else:
            print("Insufficient balance to place the order.")

    def display_customer(self):
        print(f"Customer Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Account Balance: ${self.account_balance:.2f}")
        print("Order History:")
        for order in self.orders:
            order.display_order()


# Invoice Class
class Invoice:
    """
    Represents an invoice generated for an order.
    """

    def __init__(self, invoice_id: str, order: Order):
        self.invoice_id = invoice_id
        self.order = order

    def display_invoice(self):
        print(f"Invoice ID: {self.invoice_id}")
        print("Itemized List:")
        for ebook in self.order.shopping_cart.items:
            print(f"- {ebook.title}: ${ebook.price:.2f}")
        print(f"Subtotal: ${self.order.calculate_subtotal():.2f}")
        print(f"Discounted Total: ${self.order.calculate_discounts():.2f}")
        print(f"VAT (8%): ${(self.order.calculate_total_with_vat() - self.order.calculate_discounts()):.2f}")
        print(f"Final Total (with VAT): ${self.order.calculate_total_with_vat():.2f}")
