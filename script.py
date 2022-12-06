from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys
import os
from selenium.webdriver.common.by import By
import subprocess
import pyautogui as pgui

# selenium と bs4 でonetime-passwordを取得

driver_path = r'C:\Users\341137\src\driver\chromedriver.exe'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path(driver_path))
driver.get('https://sotp.whitecloud.jp/ivpn.otp00098.ultina/ui/token.php')

title = driver.title
print(title)
driver.implicitly_wait(0.5)

driver.find_element(By.CSS_SELECTOR, '#uid').send_keys("01050341137")
driver.find_element(By.CSS_SELECTOR, "#token > input:nth-child(8)").click()

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

input_pass = ""

input_pass += str(soup.select_one('#randamNumbarTable1st > table > tbody > tr:nth-child(2) > td:nth-child(3)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable1st > table > tbody > tr:nth-child(2) > td:nth-child(4)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable2nd > table > tbody > tr:nth-child(2) > td:nth-child(1)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable2nd > table > tbody > tr:nth-child(2) > td:nth-child(2)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable2nd > table > tbody > tr:nth-child(2) > td:nth-child(3)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable2nd > table > tbody > tr:nth-child(2) > td:nth-child(4)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable3rd > table > tbody > tr:nth-child(2) > td:nth-child(1)').find('p').get_text())
input_pass += str(soup.select_one('#randamNumbarTable3rd > table > tbody > tr:nth-child(2) > td:nth-child(2)').find('p').get_text())

print(input_pass)

driver.quit()

# VPN login

subprocess.Popen(r'C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe')

time.sleep(0.5)

# pgui.press('tab')
pgui.press('enter')

time.sleep(3)

pgui.write(input_pass)

pgui.press('tab')
pgui.press('enter')