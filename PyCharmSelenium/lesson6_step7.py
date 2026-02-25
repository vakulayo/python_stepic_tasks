from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    all_inputs = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for input in all_inputs:
        input.send_keys("My answer")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(30)
    browser.quit()