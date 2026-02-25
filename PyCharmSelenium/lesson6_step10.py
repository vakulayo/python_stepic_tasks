from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input").send_keys("bla-bla-bla")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input").send_keys("bla-bla-bla")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input").send_keys("bla-bla-bla")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()