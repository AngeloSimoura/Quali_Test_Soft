from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from  webdriver_manager.chrome import ChromeDriverManager

import unittest

 
class PetPage(unittest.TestCase):

    @classmethod

    def setUpClass(inst):
        
        inst.service = Service(executable_path=ChromeDriverManager().install())
        inst.browser = webdriver.Chrome(service=inst.service)

        inst.browser.implicitly_wait(10)

        inst.browser.get("http://coral.ufsm.br/pet-si/")

 

    def test_01_open_publicacoes_page(self):

        self.browser.find_element_by_xpath("/html/body/main/div[2]/div/section/article/div/div/div/div/section[4]/div/div/div[2]/div/div/div/div/div/div[2]/h3/a").click()

        self.assertIn('notfa/sfdsf', self.browser.current_url)

        

    def test_02_search(self):

        # não é necessário navegar para 'Publicações' novamente

        self.search_field = self.browser.find_element_by_xpath("/html/body/header/div[1]/div[3]/div/div[2]/form/fieldset/div/input")

        self.search_field.send_keys("PET Redação")

        self.search_field.send_keys(Keys.ENTER) # submit query

        self.assertTrue(self.is_element_on_page(By.CLASS_NAME, 'only'))   # check for results

 

    @classmethod

    def tearDownClass(inst):

       inst.browser.quit()

 

    def is_element_on_page(self, how, what):

        try: 

            self.browser.find_element(by=how, value=what)

        except:

            return False

        return True

 
if __name__ =='__main__':
        try:
            unittest.main(verbosity=2)
        except SystemExit:
            pass