

class Book(Online_store):
    def __init__(self, json_file, store_name):
        super().__init__(json_file, store_name,)

    def display_books(self):
        data = books.read_data()
 
        for book_data in data:
             for key, value in book_data.items():
                print(f"{key}: {value}")











store = Online_store(json_file="books.json", store_name="MarsBook")
books = Book('books.json', store)
 
print(f" Store Name: {store.store_name}")


books.display()