#Тест-сьют 4: Проверка корзины

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pages.main import MainPage
from pages.cart import CartPage

import time

driver = webdriver.Chrome()
my_cart = CartPage(driver)
driver.implicitly_wait(3)
main = MainPage(driver)

prodNumber1 = 29
prodNumber2 = 31


@pytest.fixture()
def pre_test(request):
    # загрузка корзины
    my_cart.load()

    # очистка корзины
    my_cart.clear()
    time.sleep(4)

    # переход на главную
    driver.find_element(*main.TITLE).click()
    time.sleep(4)

def teardown_module(module):
    # очистка корзины
    my_cart.clear()
    driver.close()

#функция проверки общей суммы для не более двух товаров
def check_t_amount_less_three_prod(q1, q2):
    t_amount_text = driver.find_element(*my_cart.TOTAL_AMOUNT).text
    t_amount_num = float(t_amount_text.replace(' р', ''))
    prod1_price_text = driver.find_element(*my_cart.PRICE1).text
    prod1_price_num = float(prod1_price_text.replace(' р', ''))
    if q2 > 0:
        prod2_price_text = driver.find_element(*my_cart.PRICE2).text
        prod2_price_num = float(prod2_price_text.replace(' р', ''))
        assert q1*prod1_price_num + q2*prod2_price_num == t_amount_num
    else:
        assert q1 * prod1_price_num == t_amount_num



def test_cart(pre_test):
    # добавление товара 1 в корзину
    prod_buy_selector = 'a[id^= "in_cart_link_'+str(prodNumber1)+'"]'
    buy1 = driver.find_element(By.CSS_SELECTOR, prod_buy_selector).click()

    # добавление товара 2 в корзину
    prod_buy_selector = 'a[id^= "in_cart_link_'+str(prodNumber2)+'"]'
    buy2 = driver.find_element(By.CSS_SELECTOR, prod_buy_selector).click()

    # загрузка корзины
    my_cart.load()
    time.sleep(4)
    # проверка общей суммы
    check_t_amount_less_three_prod(1, 1)

    # увеличение количества товара 1 в корзине через поле ввода
    increase1 = driver.find_element(*my_cart.Q_FIELD_1).send_keys(Keys.DELETE, '3', Keys.ENTER)
    time.sleep(4)
    # проверка изменения общей суммы
    check_t_amount_less_three_prod(3, 1)

    # увеличение товара 1 в корзине стрелкой
    increase2 = driver.find_element(*my_cart.Q_FIELD_1).send_keys(Keys.ARROW_UP, Keys.ENTER)
    # проверка изменения общей суммы
    check_t_amount_less_three_prod(4, 1)

    #уменьшение товара 1 в корзине стрелкой
    decrease = driver.find_element(*my_cart.Q_FIELD_1).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    time.sleep(4)
    # проверка изменения общей суммы
    check_t_amount_less_three_prod(3, 1)

    #обнуление количества товара 2 в корзине стрелкой
    full_decrease = driver.find_element(*my_cart.Q_FIELD_2).send_keys(Keys.ARROW_DOWN)
    time.sleep(4)
    # проверка изменения общей суммы
    check_t_amount_less_three_prod(3, 0)



