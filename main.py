import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="C:/Users/Bharath/Desktop/chromedriver.exe")
browser.get("https://www.inspireawards-dst.gov.in/UserC/login.aspx?to=2")
time.sleep(5)
browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtUserId").send_keys("tumkur77")
time.sleep(5)
browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPassword").send_keys("Diet@t22")
time.sleep(5)
browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtCaptchaText").send_keys(input(str()))
time.sleep(10)
browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_imgLogin").click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="wrapper"]/div/section/div/div/div/div[1]/div/div[2]/div[2]/div/div[7]/div/h5').click()
time.sleep(5)
browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtAppCode")