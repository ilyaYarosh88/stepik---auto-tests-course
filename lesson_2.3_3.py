from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
#Формула для расчета
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#Входим на страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
#Говорим браузеру ждать пока сумма не станет 100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
#Кликаем на кнопку
browser.find_element_by_id("book").click()
#Скроллим вниз что бы отобразилась кнопка
browser.execute_script("window.scrollBy(0, 100);")
#Находим цифру
x_element = browser.find_element_by_id("input_value")
x = x_element.text
#Вычисляем по формуле
y = calc(x)
#Вводим результат в инпут
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()

time.sleep(5)
