import imp
from lib2to3.pgen2 import driver
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ["PATH"] += r"F:\selenium driver"
driver = webdriver.Chrome()
driver.get("https://www.wordproject.org/bibles/ben/index.htm?fbclid=IwAR3_y62r-VC8wVWkSRkh92Qc90UbyH47rz39nJvTyBUZjTqzM5ZDXYtHuVk")
driver.implicitly_wait(8)
#my_element = driver.find_element_by_xpath("//a[@title='[1] Genesis']")
#my_element = driver.find_element("xpath", '//*[@title="[1] Genesis"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#my_element.click()
#driver.navigate().to("https://www.wordproject.org/bibles/ben/01/1.htm") 
driver.get("https://www.wordproject.org/bibles/ben/01/1.htm")