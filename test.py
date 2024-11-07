from A2_code import *
def test_add_modify_remove_ebook():
    """Test adding, modifying, and removing e-books in the store's catalog."""
    store = EbookStore(1234567890, "shakhbout", "hamdan store")
    # Add e-books
    ebook = Ebook("physics", "ali", 29.99, "science", "Available")
    store.add_ebook(ebook)
    assert len(store.ebooks) == 1
    assert store.ebooks[0].title == "physics"
    print("Ebook added successfully.")

    # Modify e-book details
    ebook.set_price(24.99)
    assert ebook.price == 24.99
    print("Ebook price updated successfully.")

    # Remove e-book
    store.remove_ebook(ebook)
    assert len(store.ebooks) == 0
    print("Ebook removed successfully.")

def test_add_modify_remove_customer():
    """Test adding, modifying, and removing customer accounts."""
    customer = Customer ("Mansour", 1234567890, 200.0,)
    # Check initial details
    assert customer.name == "Mansour"
    assert customer.account_balance == 200.0
    print("Customer account created successfully.")

    # Modify customer details
    customer.set_name("Ali")
    assert customer.name == "Ali"
    print("Customer name updated successfully.")

    # Simulate account deletion (not implemented in this code)
    del customer
    print("Customer account removed (simulated).")

def test_add_ebooks_to_cart():
    """Test adding e-books to the shopping cart."""
    cart = ShoppingCart()
    ebook1 = Ebook("physics", "ali", 29.99, "science", "Available")
    ebook2 = Ebook("finance", "john snow", 49.99, "business", "Available")

    # Add e-books to cart
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    assert cart.get_item_count() == 2
    assert cart.get_total_amount() == 79.98
    print("Ebooks added to shopping cart successfully.")

def test_apply_discounts():
    """Test applying discounts for loyalty program members or bulk purchases."""
    cart = ShoppingCart()
    for _ in range(5):  # Add 5 e-books to qualify for bulk discount
        cart.add_item(Ebook("Book", "Author", 10.0, "Genre", "Available"))

    bulk_discount = BulkDiscount(20, "2024-01-01", "2024-12-31", 5)
    total_after_bulk_discount = bulk_discount.apply_discount(cart)
    assert total_after_bulk_discount == 40.0  # 20% off 50.0
    print("Bulk discount applied successfully.")

    old_customer_discount = OldCustomerDiscount(10, "2024-01-01", "2024-12-31", 12)
    total_after_loyalty_discount = old_customer_discount.apply_discount(total_after_bulk_discount)
    assert total_after_loyalty_discount == 36.0  # 10% off 40.0
    print("Loyalty program discount applied successfully.")

def test_invoice_generation():
    """Test the generation of an invoice showing discounts and required payments."""
    cart = ShoppingCart()
    cart.add_item(Ebook("physics", "ali", 100.0, "science", "Available"))

    # Apply a loyalty discount
    old_customer_discount = OldCustomerDiscount(10, "2024-01-01", "2024-12-31", 12)
    order = Order(1, "Completed", cart, old_customer_discount)

    # Generate invoice
    invoice = Invoice("INV001", order)
    discounted_total = order.calculate_discounts()
    total_with_vat = order.calculate_total_with_vat()

    assert invoice.invoice_id == "INV001"
    assert discounted_total == 90.0  # 10% off 100
    assert round(total_with_vat, 2) == 97.20  # 90 + 8% VAT
    print("Invoice generated successfully with correct discounts and VAT.")

def main():
    """Run all test cases."""
    print("Running Tests...\n")
    try:
        test_add_modify_remove_ebook()
        test_add_modify_remove_customer()
        test_add_ebooks_to_cart()
        test_apply_discounts()
        test_invoice_generation()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print("\nTest failed:", str(e))

if __name__ == "__main__":
    main()
