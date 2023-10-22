import json

class Online_store:
    def __init__(self, json_file, store_name):
        self.json_file = json_file
        self.store_name = store_name

    def read_data(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return []

    def write_data(self, data):
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent = 4)

    def addBook(self, new_book):
        new_book["Store_Name"] = self.store_name
        data = self.read_data()
        data.append(new_book)
        self.write_data(data)

    def remove(self, remove_bookNumber):
        data = self.read_data()
        update_data = [book for book in data if book.get("ISBN") != remove_bookNumber]
        self.write_data(update_data)
        