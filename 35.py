#------------------------------
# imports
#------------------------------
import pandas as pd
import os
from selenium import webdriver
from time import sleep
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
from time import sleep
from selenium.webdriver.chrome.options import Options
from tqdm.auto import tqdm
from multiprocessing import Process
#------------------------------
# helpers
#------------------------------
def create_dir(base,ext):
    _path=os.path.join(base,ext)
    if not os.path.exists(_path):
        os.mkdir(_path)
    return _path 

def check(element,xpath):
    '''
        checks an element by xpath
    '''
    try:
        element.find_element_by_xpath(xpath)
        return True
    except NoSuchElementException:
        return False

def waitSomeTime(mult=None):
    '''
        Waits some seconds in between high and low
    '''
    _wait_time=round(random.random()*2 + 1,2)

    if mult is None:
        sleep(_wait_time)
    else:
        for _ in range(mult):
            sleep(_wait_time)


#------------------------------
# globals
#------------------------------

chapter_title_xpath = "h1"
chapter_xpath = "h3"
bible_para_xpath = "/html/body/div[2]/div/div/div[6]/div/p"


chpt_title_lst = []
bible_para_lst = []
batch = 10


save_dir="F:\Bible"
log_txt ="/home/ansary/WORK/Research/hadithbd/log.txt"

#----------------------------
# windows
#----------------------------

os.environ["PATH"] += r"F:\selenium driver"
#driver = webdriver.Chrome('C:\\Users\\Shabab\\chromedriver')

options = Options()
prefs = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', prefs)
#  Code to disable notifications pop up of Chrome Browser
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--headless")



#----------------------------
# main page saving function
#----------------------------
def save_data(driver,spath):
    '''
        saving a single page of a sura
    '''
    global FILES,TEXTS,TZ,TB,TR
    # page
    #audio_elems=driver.find_elements(By.XPATH,audio_path)
    #text_elems =driver.find_elements(By.XPATH,arabic_xpath)
    tz_elems   =driver.find_elements(By.XPATH,bible_para_xpath)
    tb_elems   =driver.find_elements(By.XPATH,bayan_xpath)
    #xl_elems   =driver.find_elements(By.XPATH,xlation_xpath)
    
    for txt_elem,audio_elem,tz_elem,tb_elem,xl_elem in zip(text_elems,
                                                            audio_elems,
                                                            tz_elems,
                                                            tb_elems,
                                                            xl_elems):
        # save audio
        link=audio_elem.get_attribute("src")
        r = requests.get(link, allow_redirects=True)
        file_name=os.path.join(spath,os.path.basename(link))
        open(file_name, 'wb').write(r.content)
        # save arabic
        text = txt_elem.text
        # tafsir
        tzh_elem=tz_elem.find_element_by_xpath(header_xpath) #surah er starting
        header=tzh_elem.text  #surah er starting ke text e rupantor
        text_data=tz_elem.text
        text_data=text_data.replace(header,"") #surah er heading ke bad dewa

        _data=f"<header>:{header}<header>\n"
        _data+=f"<text>:{text_data}<text>"
        TZ.append(_data) #left side er para ar heading saved

        tbh_elem=tb_elem.find_element_by_xpath(header_xpath) #dan side er head
        header=tbh_elem.text
        text_data=tb_elem.text
        text_data=text_data.replace(header,"")

        _data=f"<header>:{header}<header>\n"
        _data+=f"<text>:{text_data}<text>"
        TB.append(_data) #dan side er heading para saved
        
        FILES.append(file_name) 
        TEXTS.append(text) #arabic likha gulo just save hobe
        
        xlp_elems=xl_elem.find_elements_by_xpath("p")
        xld=""
        for p in xlp_elems:
            try:
                xlt=p.text
                src=p.find_element_by_xpath(xlsrc_xpath).text
                xld+=f"##:<source>{src}<source><translation>{xlt.replace(src,'')}<translation>\n"
            except NoSuchElementException:
                with open(log_txt,"a+") as f:
                    f.write(f"Translation element incomplete at {driver.current_url} at {xlt}\n")
        TR.append(xld)