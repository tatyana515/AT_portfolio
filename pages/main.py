from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MainPage:
    URL = 'http://testshop.sedtest-school.ru/'
    TITLE = (By.CSS_SELECTOR, '#nav_link_main')
    SEARCH_BAR = (By.CSS_SELECTOR, 'input.form-control[name=search]')
    PRODUCT_LINK = (By.CSS_SELECTOR, '.text-info[href^="/product/"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[href="/users/logout/"]')
    ADD_CART = (By.CSS_SELECTOR, 'a[id^= "in_cart_link_"]')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        header = self.driver.find_element(*self.TITLE).text
        assert 'Главная' in header, "title ok"

    def search(self, phrase):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(phrase)
        self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(*self.SEARCH_BAR).send_keys(Keys.ENTER)