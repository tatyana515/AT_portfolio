from selenium.webdriver.common.by import By

class AuthPage:
    URL = 'http://testshop.sedtest-school.ru/users/auth/'
    TITLE = (By.CSS_SELECTOR, 'title')
    EMAIL_FIELD = (By.ID, 'id_email')
    PASSWORD_FIELD = (By.ID, 'id_password')
    AUTH_BUTTON = (By.TAG_NAME, 'button')


    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        header = self.driver.find_element(*self.TITLE).text
        print (header)

    def authorize(self, email, password):
        # ввод e-mail
        element = self.driver.find_element(*self.EMAIL_FIELD)
        element.clear()
        element.send_keys(email)

        # ввод пароля
        element2 = self.driver.find_element(*self.PASSWORD_FIELD)
        element2.clear()
        element2.send_keys(password)
        self.driver.implicitly_wait(5)

        #нажатие кнопки "Войти"
        self.driver.find_element(*self.AUTH_BUTTON).click()