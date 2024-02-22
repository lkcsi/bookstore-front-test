import pytest
from page import LoginPage, BooksPage, Navbar


@pytest.mark.usefixtures("setup")
def test_login(login_page: LoginPage, books_page: BooksPage):

    login_page.login("test", "password")

    assert books_page.get_title() == "Book List"


@pytest.mark.usefixtures("setup")
def test_logout(login_page: LoginPage, books_page: BooksPage, navbar: Navbar):

    login_page.login("test", "password")

    assert books_page.get_title() == "Book List"

    navbar.logout()

    assert login_page.get_title() == "Login"
