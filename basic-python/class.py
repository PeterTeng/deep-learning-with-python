class Book:
    def __init__(self, name):
        self.name = name
        print("Initialized")

    def new(self):
        print("New book: " + self.name)

    def good(self):
        print(self.name + " is a good book")

book = Book("Magic Tree House")

book.new()
book.good()
