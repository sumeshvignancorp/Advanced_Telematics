Here are the steps to download and run the script :

1. Download & Install Python : Install Python on your system if it's not already installed.
   
2. Download PyCharm :
   Visit [PyCharm Community Edition Download](https://www.jetbrains.com/pycharm/download/?section=windows) and download PyCharm (Community Edition only).

3. Install PyCharm :
   Install PyCharm Community Edition by selecting the default settings during the installation process.

4. Open the Project :
   Open the "Advanced_telematics" project in PyCharm. At the bottom of the window, ensure the Python interpreter is set to Python. If not, click on "Python 3.12" or add a new interpreter.

5. Add Required Packages :
   - Go to Main Menu -> Settings -> Project: Advanced_telematics -> Python Interpreter.
   - Click on the "Plus" icon and search for the following packages: PIP, Selenium, webdriver-manager, Pytest, Pytest-html -  Install them.

6. Run project in Existing browser :
   - https://developer.chrome.com/docs/chromedriver/  - Click 0n "the Chrome for Testing availability dashboard" - Download chrome driver of window 64
   - Download ChromeDriver.exe and Create a new folder in D-Drive as "Pytest"
   - Find path of our Chrome browser path in C-Drive as C:\Users\sumes\AppData\Local\Google\Chrome\User Data\Profile 1
   - Copy the Profile 1 folder & Paste it in Created folder "pytest"
   - Go to Chrome Application path in C drive - C:\Program Files\Google\Chrome\Application

7. Open Command prompt :
   - Step 1 > cd C:\Program Files\Google\Chrome\Application
   - Step > chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\pytest\Profile 2"
         Note - After opening browser login with Advanced telematics credentials & Don't close opened browser.

8. Add the Chromedriver.exe path in all scripts :
   - Add path of the Chromedriver.exe file 
   - As like this chrome_driver_path = "D:\\pytest\\chromedriver.exe"

9. Run the Tests :
   To run the tests, use any of the following methods:
   - Right-click on the "1smoke_testcase" directory and select Run. 
   - Alternatively, right-click on the Smoke_testcase package, open Terminal, and type any of the following commands:  
     - "pytest -v -s"
     - "pytest"
     - "pytest -v"

10. Generate a HTML Report :
    To generate a test report, right-click on the Smoke_testcase directory, open Terminal, and type:  
    "pytest --html=report.html".  
    After the execution, a file named "report.html" will appear in the project directory.

11. Generate an Allure report()
    To generate allure report >> pytest --alluredir=allure-results
    After running the above commands wait till execution completion and Run this command to view report >> allure serve allure-results

12. Run Device Script :
    Before running the 1smoke_testcase, execute the Device1.py script to generate the necessary reports.

Note -
1. While running script don't use any browser because scripts will fail

Login Credentials 
Email - sumeshhiremath13@gmail.com
Password - Ajnaview@31
