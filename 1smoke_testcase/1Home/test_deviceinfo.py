import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify Device Info page")
def test_device_info():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://login.advancedtelematics.co.uk")
    time.sleep(15)
    driver.get_screenshot_as_png()
    driver.find_element(By.XPATH, "//span[text()='Stopped']").click()  # Running [2] & Stopped [3]
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@tabindex='0'])[11]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//div[@role='button'])[12]").click()
    time.sleep(3)
    driver.save_screenshot("../Results&Status/Deviceinfo.png")
    driver.find_element(By.XPATH, "(//div[@role='button'])[13]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='View All']").click()
    time.sleep(1)
    print("Device Info & Status card displayed")
    print("URL of the page:", driver.current_url)
    time.sleep(3)
    driver.quit()
