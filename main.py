from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

website = "https://demoqa.com/login"
path = "/users/lwiltshire/downloads/chromedriver/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("demoqaUser")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password123@")
driver.find_element(By.XPATH, "//button[@id='login']").click()

#Keeps selenium running
# while 1==1:
#     pass

#this also keeps browser running
while True:
     pass
