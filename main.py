from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:/Users/Javty/Documents/Selenium Python/chromedriver_win32/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


# path to the Chrome driver executable
driver_path = "C:/Users/Javty/Documents/Selenium Python/chromedriver_win32/chromedriver.exe"

#Create a new Chrome browser instance
#driver = webdriver.Chrome(executable_path=driver_path)

#navigate to the site
driver.get("https:/demoqa.com/")

driver.close()
