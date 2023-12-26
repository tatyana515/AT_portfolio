#Тест-сьют 3: Проверка страниц товаров
from selenium import webdriver
from pages.prod import Product
from pages.prod import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#тестовые данные:

desc1 = '''Монокуляр Veber 7-21x21W ZOOM - компактный оптический прибор для наблюдения за окружающей средой 
с переменным увеличением 7х-21х. Кто сказал, что в театр ходят только с биноклем? 
Нарядный, легкий и очень компактный монокуляр Veber 7-21x21 ZOOM в белом корпусе можно взять с собой 
и на концерт, и на прогулки по городу. Он окажется у Вас под рукой в любой момент, 
когда захочется лучше рассмотреть какие-либо детали, ведь монокуляр можно держать в кармане куртки, 
в дамской сумочке или в бардачке машины.Для изготовления призмы оборачивающей системы (Roof) 
применяется стекло BАK-4 с многослойным просветлением (FMC). Линзы из оптического стекла 
(также с многослойным просветлением) объектива и окуляра обеспечивают яркое и четкое изображение даже при 
плохом освещении или в сумерках.Кольцо масштабирования размера изображения (зум) с резиновым колесом 
прокрутки находится сверху корпуса монокуляра. Параллельно ему находится диоптрийное кольцо с подстройкой
 под разное зрение.'''

pr1 = Product(31, 'Монокуляр Veber 7-21x21W ZOOM', '4', 11, 'Бр1', 'Кат1', 2130.0, 131.0, desc1)


desc2 = """Перо: нержавеющая сталь.Отделка пера: позолота 23 Kt., оригинальный перекрестный рисунок с 
гравировкой.Корпус: ювелирная латунь, покрытая эпоксидным матовым черным лаком.Система 
заправки: картриджно-конвертерная.Механизм: съемный колпачок.Отделка: покрытие высокопрочным эпоксидным лаком с
 матовой поверхностью, отдельные элементы дизайна - позолота 23 Kt.Цвет: матовый черный / золотистый.Размер 
ручки: длина ручки - 131 мм / 139 мм, максимальная ширина (диаметр) - 11 мм.Вес ручки: 35 гр."""


pr2 = Product(29, 'Ручка Паркер', '4', 12, 'Паркер', 'Ручки', 12.0, 2.01, desc2)

desc3 = """Совершенно новая машина от гугл с автопилотом!"""

pr3 = Product(17, 'Google car', '3', 3, 'Google', 'Машины', 9999999.0, 1111111.0, desc3)

catalog = [pr1, pr2, pr3]


driver = webdriver.Chrome()
prod = ProductPage(driver)
driver.implicitly_wait(3)


def test1_p():
    for i in catalog:
        # загрузка страницы очередного товара
        prod.load(i)

        # название товара
        title = driver.find_element(*prod.TITLE).text
        assert str(i.name) in title, "Название товара: " "{}".format(title)

        # категория товара
        categor = driver.find_element(*prod.CATEG).text
        assert str(i.category) in categor, "Категория товара: " "{}".format(categor)

        # заголовок страницы
        page_title = driver.title
        assert 'TestGym' in page_title, "Заголовок0: " "{}".format(page_title)

        # первоначальная цена товара
        first_price = driver.find_element(*prod.FIRST_PRIC).text
        assert str(i.price) in first_price, "Цена без скидки: " "{}".format(first_price)

        # цена со скидкой
        disc_price = driver.find_element(*prod.DISC_PRIC).text
        discount_sum0 = i.price - i.discount
        assert str(discount_sum0) in disc_price, "Цена со скидкой: " "{}".format(disc_price)

        # наличие значка корзины на верхней панели
        cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(prod.P_CART))
        assert cart

        # наличие кнопки "Добавить в корзину"
        cart_pr = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(prod.ADD_CART))
        assert cart_pr

        # наличие кнопки добавления в избранное
        favour_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(prod.ADD_FAVOURITES))
        assert favour_button

        # информация о наличии товара
        availab = driver.find_element(*prod.PROD_INFO)
        assert i.countString() in availab.text, "Наличие товара: " "{}".format(availab.text)

        # информация о картинке товара
        picture = driver.find_element(*prod.PICTURE).get_attribute("src")
        assert "/static/products/" + str(i.number) + '.png' in picture, "Картинка: " "{}".format(picture)

        # описание товара
        descrip = driver.find_element(*prod.DESCRIPT).text
        print("-- Expected: ", i.description)
        print("--   actual: ", descrip)
        assert str(i.description) in descrip, "Описание: " "{}".format(descrip)



test1_p()
