import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify Login for Reseller and Company user")
def test_summary_report():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://login.advancedtelematics.co.uk")
    time.sleep(20)

    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[@tabindex='0'])[8]").click()
    time.sleep(5)
    time.sleep(1)
    driver.find_element(By.XPATH, "(//button[@tabindex='0'])[18]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='Stopped']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@tabindex='0'])[11]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//div[@role='button'])[12]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='View All']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='Daily Summary']").click()
    time.sleep(5)
    print("URL of the page:", driver.current_url)
    time.sleep(3)
    print("Reseller Login Done")

    # Company
    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[@tabindex='0'])[8]").click()
    time.sleep(5)
    print("URL of the page:", driver.current_url)
    time.sleep(6)
    driver.find_element(By.XPATH, "(//button[@tabindex='0'])[21]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@tabindex='0'])[10]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='View All']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='Daily Summary']").click()
    time.sleep(5)
    driver.save_screenshot("../Results&Status/Company login.png")
    time.sleep(5)
    print("Company Login Done")
    driver.quit()



