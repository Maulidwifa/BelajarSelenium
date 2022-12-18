import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
fake = Faker()

class TestJob(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())


    def test_job_titles(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Job ']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Job Titles'])[1]").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Job Title']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= 'Job Description']/parent::*/following-sibling::*/child::*").send_keys(str(fake.name()))
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)

    def test_job_by_pay_grade(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text() = 'Job ']").click()
        browser.find_element(By.XPATH, "//*[text() = 'Pay Grades']").click()
        browser.find_element(By.XPATH, "//*[text() = ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text() = 'Name']/parent::*/following-sibling::*/child::*").send_keys(str(fake.pyint()))
        browser.find_element(By.XPATH, "//*[text() = ' Save ']").click()
        browser.find_element(By.XPATH, "//*[text()=' Add ']").click()
        browser.find_element(By.XPATH, "(//*[text()='Currency'])[1]/parent::*/following-sibling::*").click()
        time.sleep(5)
        # browser.execute_script("window.scrollTo(5,document.body.scrollHeight)")
        browser.find_element(By.XPATH, "//*[text() = 'AED - Utd. Arab Emir. Dirham']").click()
        time.sleep(5)
        browser.find_element(By.XPATH, "(//*[text() = 'Minimum Salary'])[1]/parent::*/following-sibling::*/child::*").send_keys("2000000")
        browser.find_element(By.XPATH, "(//*[text() = 'Maximum Salary'])[1]/parent::*/following-sibling::*/child::*").send_keys("4000000")
        browser.find_element(By.XPATH, "(//*[text() = ' Save '])[2]").click()
        time.sleep(7)

    def test_job_by_employment_status(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text() = 'Job ']").click()
        browser.find_element(By.XPATH, "(//*[text()= 'Employment Status'])[1]").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys("Magang")
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)

    def test_job_by_job_categories(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text() = 'Job ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Job Categories']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Name']/parent::*/following-sibling::*/child::*").send_keys("IT Man")
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)

    def test_job_by_work_shifts(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button").click()
        browser.find_element(By.XPATH, "//*[text() = 'Admin']").click()
        browser.find_element(By.XPATH, "//*[text() = 'Job ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Work Shifts']").click()
        browser.find_element(By.XPATH, "//*[text()= ' Add ']").click()
        browser.find_element(By.XPATH, "//*[text()= 'Shift Name']/parent::*/following-sibling::*/child::*").send_keys("Shifting")
        browser.find_element(By.XPATH, "//*[text()= 'From']/parent::*/following-sibling::*/child::*/child::*/child::i").click()
        browser.find_element(By.XPATH, "((//div[@role='alert']/child::*)[1]/child::*)[1]").click()
        browser.find_element(By.XPATH, "//*[text()= 'To']/parent::*/following-sibling::*/child::*/child::*/child::i").click()
        browser.find_element(By.XPATH, "((//div[@role='alert']/child::*)[1]/child::*)[1]").click()
        browser.find_element(By.XPATH, "//*[text()= ' Save ']").click()
        time.sleep(5)


unittest.main()