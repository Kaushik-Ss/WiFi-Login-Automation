from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import selenium
from selenium import *
import time
from PIL import Image
import io
import requests
from svgpathtools import parse_path, Line, Path, wsvg
import requests
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
url='http://172.17.0.1:2280/cportal/ip/user_login.php?url=http://www.gstatic.com/generate_204'
driver = webdriver.Chrome()


driver.maximize_window()  
driver.get(url) 
# driver.switch_to_frame("login_win")
# driver.switch_to_default_content()
driver.switch_to.frame("login_win")

driver.implicitly_wait(6)
usr_name='20I224'
pwd='20I224'
# actions = ActionChains(browser) 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://public.tableau.com/views/IsolamentoSocial/Dashboard?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=no&:toolbar=no&:animate_transition=no&:display_static_image=no&:display_spinner=no&:display_overlay=yes&:display_count=yes&:loadOrderID=1")
n = 2
actions = ActionChains(driver) 
actions.send_keys(Keys.TAB * n)
actions.send_keys(Keys.SPACE)
actions.perform()
# for _ in range(1):
#     actions = actions.send_keys(Keys.SPACE)
# actions.perform()
# driver.send_keys(Keys.SPACE) 
driver.find_element_by_css_selector("#usrname").send_keys(usr_name) 
driver.find_element_by_xpath("/html/body/div/div[1]/form/div[5]/table[1]/tbody/tr[2]/td/input").send_keys(pwd) 
# m = driver.find_element_by_xpath('/html/body/div/div[1]/form/div[5]/table[1]/tbody/tr[3]/td/label/input').click()

# driver.find_element_by_xpath('/html/body/div/div[1]/form/div[5]/table[1]/tbody/tr[3]/td/label/input').click()

# fruits = driver.find_element(By.ID, "terms").click()
# m.click()

# from selenium.webdriver import ActionChains

# actions = ActionChains(driver)
# actions.move_to_element(m).click().perform()
# time.sleep(10)

time.sleep(1)
m = driver.find_element_by_css_selector('#update_btn')
actions = ActionChains(driver)
actions.move_to_element(m).click().perform()
time.sleep(30)
