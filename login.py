from selenium import webdriver
import sys
import os
import signal
from selenium.webdriver.common.by import By


# selenium と bs4 でonetime-passwordを取得

driver_path = r'C:\Users\341137\src\driver\chromedriver.exe'
access_URL = r'https://aeonpeopleportal-web.aeonpeople.biz/workmenu/#favorite'
auth_id = '341137'
auth_pass = '3682tw'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


driver = webdriver.Chrome(resource_path(driver_path))
driver.get(access_URL)


title = driver.title
print(title)
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, '#signin > div > div > div.o-whole__body > section > div > section > div > div > button').click()
driver.find_element(By.CSS_SELECTOR, '#userNameInput').send_keys(auth_id)
driver.find_element(By.CSS_SELECTOR, '#passwordInput').send_keys(auth_pass)
driver.find_element(By.CSS_SELECTOR, '#submitButton').click()

os.kill(driver.service.process.pid,signal.SIGTERM)
print('oskill')
