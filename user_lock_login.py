from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(driver):
    driver.find_element(By.ID,"httpd_username").send_keys("admin")
    driver.find_element(By.ID,"httpd_password").send_keys("NOMUS")
    driver.find_element(By.NAME,"login").click()
    time.sleep(0.5)
    print(driver.find_element(By.ID,"erp").text)

def open_browser(driver,deviceip):
    driver.get("https://" + deviceip)
    time.sleep(2)  
    driver.find_element(By.NAME,"Continue").click()

driver = webdriver.Firefox()
open_browser(driver,deviceip="192.168.1.1")

i, j = 1, 1
sleep_time = 2 

while True:
    for _ in range(3):
        print(i,".",end=" ")
        login(driver)
        time.sleep(sleep_time)
        i += 1
    sleep_time += 2
    if sleep_time > 20:
        sleep_time = 2

    j += 1
#     print(f"Cycle {j} completed, next sleep time: {sleep_time} seconds")
