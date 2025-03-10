import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify the Add Device page by entering the IMEI and other required details.")
def test_add_device():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://login.advancedtelematics.co.uk/")
    time.sleep(10)
    driver.find_element("xpath", "(//button[@type='button'])[7]").click()
    time.sleep(6)
    # Device_details
    driver.find_element(By.XPATH, "(//input[@aria-invalid='false'])[1]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@aria-label='Clear'])[1]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//input[@aria-invalid='false'])[1]").send_keys("Reseller 1")
    time.sleep(1)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ARROW_DOWN)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element("xpath", "(//input[@type='text'])[3]").send_keys("Testing zz")
    driver.find_element("xpath", "(//input[@type='text'])[4]").send_keys("0000000005785")  # 808800005786, 808800005785
    time.sleep(1)
    driver.find_element("xpath", "(//input[@type='text'])[5]").send_keys("FM00012")
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='text'])[6]").send_keys("user")
    driver.find_element("xpath", "(//input[@type='text'])[7]").send_keys("8985969855")
    time.sleep(1)
    print("URL of the page:", driver.current_url)
    time.sleep(1)
    # Vehicle details
    driver.find_element("xpath", "(//input[@type='text'])[9]").send_keys("23455")
    driver.find_element("xpath", "(//input[@type='text'])[10]").send_keys("KA01 AB 1234")
    time.sleep(2)
    driver.find_element("xpath", "(//div[@role='combobox'])[3]").click()
    driver.find_element("xpath", "(//li[@role='option'])[1]").click()
    driver.find_element("xpath", "(//input[@type='number'])[1]").send_keys("104")
    driver.find_element("xpath", "(//input[@type='number'])[2]").send_keys("40")
    driver.find_element("xpath", "(//input[@type='number'])[3]").send_keys("23")
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='text'])[12]").send_keys("12345")
    driver.find_element("xpath", "(//input[@type='text'])[13]").send_keys("12345")
    driver.find_element("xpath", "(//input[@type='text'])[14]").send_keys("M2M Sim")
    time.sleep(2)
    driver.find_element("xpath", "//button[text()='Save']").click()
    time.sleep(3)
    driver.get_screenshot_as_file("../Results&Status/5New device added.png")
    print("Device added")
    time.sleep(1)

    # delete device
    driver.find_element("xpath", "//input[@placeholder='Search Devices']").send_keys("Testing zz")
    time.sleep(12)
    driver.find_element(By.XPATH, "(//div[@tabindex='0'])[10]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//div[@role='button'])[11]").click()
    time.sleep(1)
    driver.find_element("xpath", "(//button[@type='button'])[8]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[text()='Remove']").click()
    time.sleep(3)
    driver.get_screenshot_as_file("../Results&Status/6Delete confirmation.png")
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "//button[text()='Yes']")
    actions.click(demo).perform()
    time.sleep(3)
    driver.get_screenshot_as_file("../Results&Status/7Device deleted.png")
    print('Add/Delete Device Passed and Captured')
    time.sleep(2)
    driver.quit()
