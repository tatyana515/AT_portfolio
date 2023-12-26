from selenium.webdriver.common.by import By



class CartPage:
    URL = 'http://testshop.sedtest-school.ru/mycart/'
    TITLE = (By.CSS_SELECTOR, 'div.container > h3')
    Q_FIELD = (By.CSS_SELECTOR, 'input[id^= "count_"]')
    Q_FIELD_1 = (By.CSS_SELECTOR, 'body > div.container > div > div.col-md-10 > div:nth-child(1) > \
                 div > div > div > div:nth-child(2) input')
    Q_FIELD_2 = (By.CSS_SELECTOR, 'body > div.container > div > div.col-md-10 > div:nth-child(3) > \
                 div > div > div > div:nth-child(2) input')
    DELETE_BUTTON_PART = (By.CSS_SELECTOR, 'a[href^= "/mycart/change_count/')
    FIRST_DELETE_BUTTON = (By.CSS_SELECTOR, '.col-md-10 > .media:nth-child(1) .media-body .row > div:nth-child(4)>a')
    TOTAL_AMOUNT = (By.CSS_SELECTOR, '.container > div > div.col-md-2 > span:nth-child(3)')
    PRICE1 = (By.CSS_SELECTOR, 'body > div.container > div > div.col-md-10 > div:nth-child(1) >  \
                div > div > div > div.col-md-3 > span:nth-child(1)')
    PRICE2 = (By.CSS_SELECTOR, 'body > div.container > div > div.col-md-10 > div:nth-child(3) > \
            div > div > div > div.col-md-3 > span:nth-child(1)')



    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        header = self.driver.find_element(*self.TITLE).text
        assert 'Ваша корзина' in header, "title ok"



    def clear(self):
        num = self.driver.find_elements(*self.DELETE_BUTTON_PART)
        if len(num) > 0:
            for i in range(1, len(num)+1):
                clean = self.driver.find_element(*self.FIRST_DELETE_BUTTON).click()

