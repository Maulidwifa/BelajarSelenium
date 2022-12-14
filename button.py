from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def setUp(self):
    self.driver = webdriver.Chrome()

class TestCaseBelanja(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    elem = driver.find_element(By.NAME, "user-name")
    elem.send_keys("standard_user")
    elem = driver.find_element(By.NAME, "password")
    elem.send_keys("secret_sauce")
    elem = driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    elem = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(5)
    elem = driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(5)
    elem = driver.find_element(By.ID, "checkout").click()
    time.sleep(5)
    elem = driver.find_element(By.NAME, "firstName")
    elem.send_keys("Maulidwifa")
    time.sleep(5)
    elem = driver.find_element(By.NAME, "lastName")
    elem.send_keys("Fairuz")
    time.sleep(5)
    elem = driver.find_element(By.NAME, "postalCode")
    elem.send_keys("Sauce-Backpack")
    time.sleep(5)
    elem = driver.find_element(By.ID, "continue").click()
    time.sleep(5)
    elem = driver.find_element(By.ID, "finish").click()
    time.sleep(5)

    