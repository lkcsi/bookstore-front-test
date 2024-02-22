from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True

    locators = {
        "username": ("ID", "username"),
        "password": ("ID", "password"),
        "login_btn": ("ID", "login"),
        "title": ("ID", "login-title"),
    }

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_submit()

    def get_title(self) -> str:
        return self.title.get_text()

    def set_username(self, username):
        self.username.set_text(username)

    def set_password(self, password):
        self.password.set_text(password)

    def click_submit(self):
        self.login_btn.click()
