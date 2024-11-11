from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    a_element, b_element = browser.find_element(By.ID, "num1"), browser.find_element(By.ID, "num2")
   # b_element = browser.find_element(By.ID, "num2")
    text1, text2 = a_element.text, b_element.text
    #text2 = b_element.text
    #y = int(text1) + int(text2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(int(text1) + int(text2)))

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

#