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

    driver.find_element("xpath", "(//div[@role='button'])[8]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[@tabindex='0'])[8]").click()
    time.sleep(5)
    time.sleep(1)
    driver.find_element(By.XPATH, "(//button[@tabindex='0'])[18]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@tabindex='0'])[13]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//div[@role='button'])[14]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[4]/div[2]/button").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[5]/div[1]/div/button[2]").click()
    time.sleep(5)
    print("URL of the page:", driver.current_url)
    time.sleep(3)
    print("Reseller Login Done")

    # Company
    driver.find_element("xpath", "(//div[@role='button'])[8]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[@tabindex='0'])[8]").click()
    time.sleep(5)
    print("URL of the page:", driver.current_url)
    time.sleep(1)
    driver.find_element(By.XPATH, "(//button[@tabindex='0'])[21]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div").click()
    driver.save_screenshot("../Results&Status/Company login.png")
    time.sleep(5)
    print("Company Login Done")
    driver.quit()



