class Author:
    _instances = []

    def __init__(self, name):
        self._name = None 
        self.name = name 
        Author._instances.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def __str__(self):
        return self.name

    def contracts(self):
        """Return a list of contracts related to this author."""
        return [contract for contract in Contract.all_instances() if contract.author == self]

    def books(self):
        """Return a list of books related to this author via contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object between the author and the specified book."""
        if not isinstance(book, Book):
            raise ValueError("The book must be an instance of the Book class.")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        """Return the total amount of royalties the author has earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())

    @classmethod
    def all_instances(cls):
        return cls._instances


class Book:
    _instances = []

    def __init__(self, title):
        self._title = None  # Use private attribute for controlled access
        self.title = title  # Use setter to initialize title
        Book._instances.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Title must be a non-empty string.")
        self._title = value

    def __str__(self):
        return self.title

    @classmethod
    def all_instances(cls):
        return cls._instances


class Contract:
    _instances = []

    def __init__(self, author, book, date, royalties):
        self.author = author  # Use setter to initialize author
        self.book = book      # Use setter to initialize book
        self.date = date      # Use setter to initialize date
        self.royalties = royalties  # Use setter to initialize royalties
        Contract._instances.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise ValueError("Book must be an instance of the Book class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Date must be a non-empty string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Royalties must be a non-negative number.")
        self._royalties = value

    def __str__(self):
        return (f"Contract Details:\n"
                f"Author: {self.author}\n"
                f"Book: {self.book}\n"
                f"Date: {self.date}\n"
                f"Royalties: {self.royalties}%")

    @classmethod
    def all_instances(cls):
        return cls._instances

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date as the date passed into the method."""
        return [contract for contract in cls.all_instances() if contract.date == date]

# Example Usage
author = Author("Harper Lee")
book1 = Book("To Kill a Mockingbird")
book2 = Book("Another Book")

# Creating contracts
contract1 = author.sign_contract(book1, "2024-09-16", 5)
contract2 = author.sign_contract(book2, "2024-09-16", 7)
contract3 = author.sign_contract(book1, "2024-10-01", 6)

# Fetch contracts by date
contracts_on_sep_16 = Contract.contracts_by_date("2024-09-16")
print("Contracts on 2024-09-16:")
for contract in contracts_on_sep_16:
    print(contract)
