import pytest
from selenium import webdriver
from page import LoginPage, BooksPage, Navbar


@pytest.fixture(scope="function")
def driver():
    return webdriver.Chrome()


@pytest.fixture(scope="function")
def setup(driver: webdriver.Chrome):
    driver.get("http://localhost:8082")
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def books_page(driver):
    return BooksPage(driver)


@pytest.fixture(scope="function")
def navbar(driver):
    return Navbar(driver)
