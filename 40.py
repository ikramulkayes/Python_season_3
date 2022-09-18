from cgitb import text
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager
import tqdm
import pandas as pd


os.environ["PATH"] += r"F:\selenium driver"

driver = webdriver.Chrome(ChromeDriverManager().install())
#url = f"https://www.wordproject.org/bibles/ben/{elm}/1.htm#0"
#driver.get("https://www.wordproject.org/bibles/ben/01/1.htm#0")

bible_para_xpath = "/html/body/div[2]/div/div/div[6]/div/p"
chapter_title_xpath = "/html/body/div[2]/div/div/div[1]/h1"
chapter_xpath = "/html/body/div[2]/div/div/div[4]/div/div/div[2]/div[2]/ul/li/a"

bible_para_lst = []
chapter_title = []
chapter_name = []
chapter_no = []
verse_no = []


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
            chapter_title_web = driver.find_element(By.XPATH,chapter_title_xpath)
            chapter_title.append(chapter_title_web.text) #chapter name only 

            chapter_name_web = driver.find_element(By.XPATH,chapter_xpath)
            chapter_name.append(chapter_name_web.text)  #chapter name boro



            chapter_no.append(k)
            verse_no.append(l)

            elem = driver.find_elements(By.XPATH,bible_para_xpath)

            print("#################")
            #print(elem)
            word = ""
            for elm in elem:
                result = ''.join([i for i in elm.text if not i.isdigit()])
                word += result + '\n'
            word = word.rstrip("\n")
            bible_para_lst.append(word)
            print("##############")

data = {
    "citation":chapter_name,
    "book":chapter_title,
    "chapter":chapter_no,
    "verse": verse_no,
    "text":bible_para_lst
}
df = pd.DataFrame(data,index=False)
print(df)
#df.to_csv (r'F:\Bible\export_dataframe.csv', index = False, header=True)

        


    