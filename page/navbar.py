from seleniumpagefactory.Pagefactory import PageFactory


class Navbar(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "logout_btn": ("ID", "logout"),
    }

    def logout(self):
        self.logout_btn.click()
