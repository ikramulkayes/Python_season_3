from cgitb import text
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager



os.environ["PATH"] += r"F:\selenium driver"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.wordproject.org/bibles/ben/01/1.htm#0")
        #self.assertIn("Python", driver.title)
bible_para_xpath = "/html/body/div[2]/div/div/div[6]/div/p"
elem = driver.find_elements(By.XPATH,bible_para_xpath)
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)
print("#################")
print(elem)
for elm in elem:
    print(elm.text)


print("##############")