import pytest
from page import LoginPage, BooksPage, Navbar
from entity import Book
from client import BookClient


@pytest.mark.usefixtures("setup")
def test_books_items(login_page: LoginPage, books_page: BooksPage):

    login_page.login("test", "password")

    assert books_page.get_title() == "Book List"

    book_client = BookClient()

    resp_items = book_client.find_all().json()

    resp_items = [Book(**book) for book in resp_items]

    page_items = [books_page.get_book(book.id) for book in resp_items]

    assert set(resp_items).issubset(set(page_items))
