import pytest
from biblioteka_wsb.Library import Library
from biblioteka_wsb.Book import Book

@pytest.fixture
def test_book():
    test_book = Book("Test Book", "Test Author", 2020, 1234567890)
    return test_book

@pytest.fixture
def test_library():
    test_library = Library("Test Library")
    return test_library

def test_library__str__(test_library):
    assert str(test_library) == "Library Test Library with 0 books"

def test_library__repr__(test_library):
    assert repr(test_library) == "Library('Test Library')"


def test_add_book(test_book, test_library):
    test_library.add_book(test_book)
    assert test_book in test_library.books



def test_find_book(test_book, test_library):
    test_library.add_book(test_book)
    assert test_library.find_book("Test Book") == test_book

def test_find_books(test_book, test_library):
    test_library.add_book(test_book)
    assert test_library.find_books(test_book.author) == [test_book]


def test_find_books_by_year(test_book, test_library):
    test_library.add_book(test_book)
    assert test_library.find_books_by_year(test_book.year) == [test_book]


def test_find_books_by_isbn(test_book, test_library):
    test_library.add_book(test_book)
    assert test_library.find_books_by_isbn(test_book.isbn) == [test_book]


def test_find_books_by_title(test_book, test_library):
    test_library.add_book(test_book)
    assert test_library.find_books_by_title(test_book.title) == [test_book]

def test_find_books_by_author(test_book, test_library):
    test_library.add_book(test_book)
    assert test_library.find_books_by_author(test_book.author) == [test_book]


def test_remove_book(test_book, test_library):
    test_library.add_book(test_book)
    test_library.remove_book(test_book)
    assert test_book not in test_library.books
