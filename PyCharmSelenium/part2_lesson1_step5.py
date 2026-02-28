from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    time.sleep(10)
    browser.quit()