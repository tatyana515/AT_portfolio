#Тест-сьют 1: Авторизация пользователя
import pytest
from selenium import webdriver
from pages.auth import AuthPage
from pages.main import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
auth = AuthPage(driver)
test_email = 'testmail@gmail.com'
test_password = 'tm1234'
driver.implicitly_wait(5)

@pytest.fixture()
def pre_test(request):
    auth.load()

def teardown_module(module):
    driver.close()


def check_auth():
    # загрузка страницы с товарами
    element = driver.find_element(*MainPage.PRODUCT_LINK)

    # появление кнопки 'Выйти'
    element2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.LOGOUT_BUTTON))
    but = driver.find_element(*MainPage.LOGOUT_BUTTON).text
    assert 'Выйти' in but, "Надпись справа вверху страницы: " "{}".format(but)


def test_auth(pre_test):
    auth.authorize(test_email, test_password)
    check_auth()




