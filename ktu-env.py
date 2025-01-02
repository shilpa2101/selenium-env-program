from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
driver=webdriver.Chrome()
# Load the .env file
load_dotenv()

# Verify environment variables

username = os.getenv("KTU_USERNAME")
password = os.getenv("KTU_PASSWORD")


print(f"KTU_USERNAME: {username}")
print(f"KTU_PASSWORD: {password}")

try:
    driver.get("https://app.ktu.edu.in/login.htm")
    time. sleep(2)
    username=driver.find_element(By.NAME,"username").send_keys(username)
    password=driver.find_element(By.NAME,"password")
    password.send_keys(password)
    time.sleep(2)
    password.send_keys(Keys.ENTER)
    time.sleep(2)
finally:
    driver.quit()
