class Author: 
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("Royalties must be a number")
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract: 
    all = []
    
    def __init__(self, author, book, date, royalties): 
        self.author = None
        self.book = None
        self.date = None
        self.royalties = None

        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)
        
        Contract.all.append(self)

    def set_author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        self.author = author

    def set_book(self, book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        self.book = book

    def set_date(self, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        self.date = date

    def set_royalties(self, royalties):
        if not isinstance(royalties, (int, float)):
            raise Exception("Royalties must be a number")
        self.royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        return [contract for contract in cls.all if contract.date == date]