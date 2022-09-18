import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager

os.environ["PATH"] += r"F:\selenium driver"
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        #driver = self.driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.wordproject.org/bibles/ben/01/1.htm#0")
        #self.assertIn("Python", driver.title)
        bible_para_xpath = "/html/body/div[2]/div/div/div[6]/div/p"
        elem = driver.find_elements(By.XPATH, bible_para_xpath)
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)
        print("#################")
        print(elem)
        count = 1
        for elm in zip(elem):
            print(count)
            count += 1
        print("##############")
            


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
print(__name__)