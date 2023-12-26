#Тест-сьют 2: Поиск с главной страницы и повторный поиск
import pytest
from selenium import webdriver
from pages.main import MainPage


driver = webdriver.Chrome()
main = MainPage(driver)
driver.implicitly_wait(3)

@pytest.fixture()
def pre_test(request):
    main.load()

def teardown_module(module):
    driver.close()

#проверка результатов поиска
def check_search(phrase):
    elems = driver.find_elements(*main.PRODUCT_LINK)
    for i in range (0, len(elems)):
        assert phrase in elems[i].text, phrase+'содержится в наименовании продукта'



def test_search_parker(pre_test):
    main.search('Паркер')
    check_search('Паркер')

def test_search_car():
    main.search('car')
    check_search('car')