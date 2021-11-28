import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# pytest -v --driver Chrome --driver-path /chromedriver_win/chromedriver test_all_pets.py


def test_all_pets():
    """Проверяем карточки всех питомцев на главной странице сайта и добавляем неявные ожидания всех элементов"""
    # Неявное ожидание
    pytest.driver.implicitly_wait(5)
    # Нажимаем кнопку "Войти"
    pytest.driver.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]').click()
    # Проверяем, что находимся на главной странице пользователя
    assert pytest.driver.find_element(by=By.TAG_NAME, value='h1').text == "PetFriends"
    # Переменная с явным ожиданием для поиска фото, имён, возраста питомцев на странице
    pet_photo = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located(
        (By.XPATH, '//img[@class="card-img-top"]')))
    pet_names = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located(
        (By.XPATH, '//h5[@class="card-title"]')))
    pet_ages = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located(
        (By.XPATH, '//p[@class="card-text"]')))
    # Проверяем, что на странице есть фото, имена и возраст питомцев и эти данные не являются "пустой строкой":
    for i in range(len(pet_names)):
        assert pet_names[i].text != '', "Не у всех питомцев заполнено имя"
        assert pet_ages[i].text != '', "Не у всех питомцев указан возраст"
        assert pet_photo[i].get_attribute('src') != '', "Не укаждого питомца загружено фото"


def test_my_pets():
    """Проверяем карточки питомцев на странице "Мои питомцы" и добовляем явные ожидания элементов страницы"""
    # Нажимаем кнопку "Войти"
    pytest.driver.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]').click()
    # Нажимаем кнопку "Мои питомцы"
    pytest.driver.find_element(by=By.LINK_TEXT, value='Мои питомцы').click()
    # Проверяем, что находимся в своём аккаунте
    assert pytest.driver.find_element(by=By.TAG_NAME, value='h2').text == 'Dim80', "Вы входите не в свой аккаунт"
    # Ищем в таблице все строки у питомцев(Фото, Имя, Порода, Возраст, значек удаления "х")
    all_my_pets = pytest.driver.find_elements(by=By.CSS_SELECTOR, value='tbody>tr')
    # Проверяем, что все питомцы видны на странице
    for i in range(len(all_my_pets)):
        assert WebDriverWait(pytest.driver, 5).until(EC.visibility_of(all_my_pets[i]))
    # Ищем в таблицы все фотографии питомцев
    photo_my_pets = pytest.driver.find_elements(by=By.XPATH, value='//th/img')
    # Проверяем, что все фото питомцем видны на странице и имею фото
    for i in range(len(photo_my_pets)):
        assert WebDriverWait(pytest.driver, 5).until(EC.visibility_of(photo_my_pets[i])), \
            "Не укаждого питомца загружено фото"
    # Ищем в таблице все имена питомцев
    name_my_pets = pytest.driver.find_elements(by=By.XPATH, value='//td[1]')
    # Проверяем, что имена питомцев видны на странице и имя заполнено
    for i in range(len(name_my_pets)):
        assert WebDriverWait(pytest.driver, 5).until(EC.visibility_of(name_my_pets[i])), \
            "Не у всех питомцев заполнено имя"
    # Ищем в таблицы все данные о возрастах питомцев
    age_my_pets = pytest.driver.find_elements(by=By.XPATH, value='//td[3]')
    # Проверяем, что все возраста питомцем видны на странице и заполнен возраст
    for i in range(len(age_my_pets)):
        assert WebDriverWait(pytest.driver, 5).until(EC.visibility_of(age_my_pets[i])), \
            "Не у всех питомцев указан возраст"
