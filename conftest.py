import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    # Для тестирования используем драйвер Chrome
    pytest.driver = webdriver.Chrome('/chromedriver_win/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email
    pytest.driver.find_element(by=By.ID, value='email').send_keys('136-06@mail.ru')
    # Вводим пароль
    pytest.driver.find_element(by=By.ID, value='pass').send_keys('12345678')

    yield

    pytest.driver.quit()
