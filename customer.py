class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.shopping_cart = []

    def add_to_cart(self, item_book):
        self.shopping_cart.append(item_book)

    def view_cart(self):
        return self.shopping_cart
    
    def checkout(self):
        print(f"{self.customer_name}'s purchase has been completed. Thank You!")

customer = Customer("John Doe")
print(f"Customer Name: {customer.customer_name}")

print("Books on the store:")
Book.display_books()

customer.add_to_cart({
    "Title": "Another Book",
    "Author": "Author Name",
    "ISBN": "978-2222222222",
    "Publication_Year": "2022",
    "Availability": "In Stock",
    "Genre": "Fiction"
})

print(f"{customer.customer_name}'s Shopping Cart:")
for book in customer.view_cart():
    print(book)

customer.checkout()