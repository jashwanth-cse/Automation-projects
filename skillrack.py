from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.skillrack.com/faces/candidate/trackshome.xhtml")
driver.maximize_window()
login_id=driver.find_element(By.XPATH,'//*[@id="j_id_7"]/div/div/form[2]/table/tbody/tr[1]/td/div/input')
login_id.send_keys("") #your skillrack username
time.sleep(1)
password=driver.find_element(By.XPATH,'//*[@id="j_id_7"]/div/div/form[2]/table/tbody/tr[2]/td/div/input')
password.send_keys("") #your skillrack password
login_box=driver.find_element(By.XPATH,'//*[@id="j_id_7"]/div/div/form[2]/input')
login_box.click()
input("Press any key to close")

