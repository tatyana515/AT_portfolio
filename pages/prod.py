from selenium.webdriver.common.by import By



class Product:
    def __init__(self, number, name, ranking, quantity, maker, category, price, discount, description):
        self.number = number
        self.name = name
        self.ranking = ranking
        self.quantity = quantity
        self.maker = maker
        self.category = category
        self.price = price
        self.discount = discount
        self.description = description.replace('\n', ' ').replace('\r', '').replace('  ', ' ')

    def countString(self):
        availability = ""
        if self.quantity == 0:
            availability = "Нет в наличии"
        elif self.quantity in range(1, 4):
            availability = "В наличии мало"
        elif self.quantity in range(4, 11):
            availability = "В наличии немного"
        elif self.quantity >= 11:
            availability = "В наличии"
        return availability


class ProductPage:
    URL_PART = 'http://testshop.sedtest-school.ru/product/'
    TITLE = (By.CSS_SELECTOR, '.card-title>span')
    CATEG = (By.CSS_SELECTOR, 'h5>a')
    FIRST_PRIC = (By.CSS_SELECTOR, '.card-body>.row>div:nth-child(2)>span:nth-child(3)')
    DISC_PRIC = (By.CSS_SELECTOR, '.card-body>.row>div:nth-child(2)>span:nth-child(1)')
    P_CART = (By.CSS_SELECTOR, 'a[href= "/mycart/"]')
    ADD_CART = (By.CSS_SELECTOR, 'a[id^= "in_cart_link_"]')
    ADD_FAVOURITES = (By.CSS_SELECTOR, 'a[id^= "in_star_link_"]')
    PROD_INFO = (By.CSS_SELECTOR, '.card-body:nth-child(1) .col-md-6:nth-child(1)')
    PICTURE = (By.CSS_SELECTOR, 'img[src^="/static/products/"]')
    DESCRIPT = (By.CSS_SELECTOR, '.card-body>p')

    def __init__(self, driver):
        self.driver = driver

    def load(self, testPr):
        self.driver.get(self.URL_PART + str(testPr.number))
        self.driver.implicitly_wait(3)
        prod_name = self.driver.find_element(*self.TITLE).text
        assert str(testPr.name) in prod_name, "Название товара: " "{}".format(prod_name)



