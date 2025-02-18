import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify the Route Report functionality, including XLSX and PDF downloads, Mail Report, Scheduled Report, and Show Report options")
def test_route_report():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://login.advancedtelematics.co.uk/")
    time.sleep(10)

    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    time.sleep(2)
    driver.find_element("xpath", "(//a[@tabindex='0'])[3]").click()  # route
    time.sleep(5)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[text()='Today']").click()
    driver.find_element("xpath", "(//input[@role='combobox'])").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys("evd")
    time.sleep(2)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ARROW_DOWN)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='Show']").click()
    time.sleep(8)
    print("URL of the page:", driver.current_url)
    # Export
    driver.find_element(By.XPATH, "//button[text()='Export']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[text()='XLSX']").click()
    print("Xlsx file downloaded")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Export']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='PDF']").click()
    time.sleep(3)
    # Email report
    driver.find_element(By.XPATH, "//button[text()='Email Report']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='XLSX']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    print("Xlsx file sent to Email")
    driver.find_element(By.XPATH, "//button[text()='Email Report']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[text()='PDF']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    print("Pdf file sent to Email")
    time.sleep(3)
    print('Route_Report Passed and Captured')
    print("URL of the page:", driver.current_url)
    time.sleep(3)
    driver.quit()
