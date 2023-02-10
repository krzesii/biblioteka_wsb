import pytest
from biblioteka_wsb.Book import Book


@pytest.fixture
def test_book():
    test_book = Book("Test Book", "Test Author", 2020, 1234567890)
    return test_book


@pytest.fixture
def test_book_eq():
    test_book_eq = Book("Test Book", "Test Author", 2020, 1234567890)
    return test_book_eq

@pytest.fixture
def test_book_neq():
    test_book_neq = Book("Test Book 2", "Test Author 2", 2022, 1234)
    return test_book_neq


def test_book__str__(test_book):
    assert str(test_book) == "Test Book by Test Author (2020)"


def test_book__repr__(test_book):
    assert repr(test_book) == "Book('Test Book', 'Test Author', 2020, 1234567890)"


def test_book__eq__(test_book, test_book_eq, test_book_neq):
    assert test_book == test_book_eq
    assert test_book != test_book_neq
