from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from entity import Book


class BookItem:
    def __init__(self, web_element):
        self.web_element = web_element

    locators = {
        "title": (By.ID, "book-title"),
        "author": (By.ID, "book-author"),
        "quantity": (By.ID, "book-quantity"),
    }

    def title(self) -> str:
        return self.web_element.find_element(*self.locators["title"]).text

    def author(self) -> str:
        return self.web_element.find_element(*self.locators["author"]).text

    def quantity(self) -> int:
        string = self.web_element.find_element(*self.locators["quantity"]).text
        return int(string)


class BooksPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "title": ("ID", "books-title"),
    }

    def get_title(self) -> str:
        return self.title.text

    def get_book(self, book_id: str) -> Book:
        elem = self.driver.find_element(By.ID, f"book-{book_id}")
        book_item = BookItem(elem)

        return Book(
            id=book_id,
            title=book_item.title(),
            author=book_item.author(),
            quantity=book_item.quantity(),
        )
