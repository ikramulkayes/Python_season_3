from cgitb import text
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager
import tqdm


os.environ["PATH"] += r"F:\selenium driver"

driver = webdriver.Chrome(ChromeDriverManager().install())
#url = f"https://www.wordproject.org/bibles/ben/{elm}/1.htm#0"
#driver.get("https://www.wordproject.org/bibles/ben/01/1.htm#0")

bible_para_xpath = "/html/body/div[2]/div/div/div[6]/div/p"
for k in (range(1,67,1)):
    flag = True
    k = str(k)
    if len(k) == 1:
        k = "0"+k
    for l in range(1,51):
        if flag == False:
            break
        url = f"https://www.wordproject.org/bibles/ben/{k}/{l}.htm#0"
        driver.get(url)
        driver.implicitly_wait(5)
        try:
            yoyo = driver.find_element(By.XPATH,"/html/body/center[1]/h1")
            if yoyo.text == "404 Not Found":
                flag = False
                break
        except:

            elem = driver.find_elements(By.XPATH,bible_para_xpath)

            print("#################")
            print(elem)
            for elm in elem:
                print(elm.text)
        


    print("##############")