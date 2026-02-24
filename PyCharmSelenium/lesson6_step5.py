from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_link = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link_local = browser.find_element(By.LINK_TEXT, text_link)
    link_local.click()

    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")

    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
