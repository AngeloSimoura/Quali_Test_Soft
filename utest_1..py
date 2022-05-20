import os
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from  webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

import unittest

 
class PetPage(unittest.TestCase):

    @classmethod

    def setUpClass(inst):
        
        inst.service = Service(executable_path=ChromeDriverManager().install())
        inst.browser = webdriver.Chrome(service=inst.service)
        inst.browser.implicitly_wait(10)

        inst.browser.maximize_window()
        inst.wait=WebDriverWait(inst.browser,10)

        inst.browser.get("https://demoqa.com/")

 

    def test_01_open_forms_page(self):

        element=self.browser.find_element(By.XPATH,"//*[text()='Forms']")
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.assertIn('forms', self.browser.current_url)

        

    def test_02_click_practice_form_page(self):

        self.wait.until(EC.element_to_be_clickable(self.browser.find_element(By.XPATH,"//*[text()='Practice Form']")))
        time.sleep(2)
        practiceFormElement=self.browser.find_element(By.XPATH,"//*[text()='Practice Form']")
        practiceFormElement.click()

        self.assertIn('automation-practice-form', self.browser.current_url)

    def test_03_fill_form(self):
        # get Elements
        firstNameElement=self.browser.find_element(By.ID,"firstName")
        lastNameElement=self.browser.find_element(By.ID,"lastName")
        txtMailElement=self.browser.find_element(By.ID,"userEmail")
        radioBTGenderFemale=self.browser.find_element(By.XPATH,"//*/label[text()='Female']")
        radioBTGenderMale=self.browser.find_element(By.XPATH,"//*/label[text()='Male']")
        radioBTGenderOther=self.browser.find_element(By.XPATH,"//*/label[text()='Other']")
        txtNumber=self.browser.find_element(By.ID,"userNumber")
        txtDateBirth=self.browser.find_element(By.ID,'dateOfBirthInput')
        txtSubjects=self.browser.find_element(By.ID,"subjectsInput")
        checkBoxHobbiesSports=self.browser.find_element(By.XPATH,"//*/label[text()='Sports']")
        checkBoxHobbiesReading=self.browser.find_element(By.XPATH,"//*/label[text()='Reading']")
        checkBoxHobbiesMusic=self.browser.find_element(By.XPATH,"//*/label[text()='Music']")
        pictureElement=self.browser.find_element(By.ID,"uploadPicture")
        txtCurrentAddress=self.browser.find_element(By.ID,"currentAddress")
        selectState=self.browser.find_element(By.XPATH,"//*[text()='Select State']")
        selectCity=self.browser.find_element(By.XPATH,"//*[text()='Select City']")
        buttonSubmit=self.browser.find_element(By.ID,"submit")
        scrlDwnELement=self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/span/div")
        
        # fill Elements
        firstNameElement.send_keys("Teste")
        lastNameElement.send_keys("Teste")
        txtMailElement.send_keys("teste@teste.com")
        radioBTGenderMale.click()
        txtNumber.send_keys("0123456789")
        txtDateBirth.click()
        self.wait.until(EC.element_to_be_clickable(self.browser.find_element(By.CLASS_NAME,"react-datepicker__month-select")))
        monthPicker=Select(self.browser.find_element(By.CLASS_NAME,"react-datepicker__month-select"))
        monthPicker.select_by_value('0')
        self.wait.until(EC.element_to_be_clickable(self.browser.find_element(By.CLASS_NAME,"react-datepicker__year-select")))
        yearPicker=Select(self.browser.find_element(By.CLASS_NAME,"react-datepicker__year-select"))
        yearPicker.select_by_value('1998')
        valor='10'
        try:
            dayPicker=self.browser.execute_script(f"return document.getElementsByClassName('react-datepicker__day react-datepicker__day--0{valor}')[0]")
        except Exception as e:
            dayPicker=self.browser.execute_script(f"return document.getElementsByClassName('react-datepicker__day react-datepicker__day--0{valor} react-datepicker__day--weekend')[0]")           
        dayPicker.click()
        txtSubjects.send_keys("Computer Science")
        txtSubjects.send_keys(Keys.ENTER)
        self.browser.execute_script("arguments[0].scrollIntoView();", scrlDwnELement)
        self.browser.execute_script("arguments[0].scrollIntoView();", checkBoxHobbiesSports)
        checkBoxHobbiesSports.click()
        self.browser.execute_script("arguments[0].scrollIntoView();", pictureElement)
        pictureElement.send_keys(os.getcwd()+"/picture.jpg")
        time.sleep(1)
        txtCurrentAddress.send_keys("Teste")
        self.browser.execute_script("arguments[0].scrollIntoView();", scrlDwnELement)
        scrlDwnELement.click()
        self.browser.execute_script("arguments[0].scrollIntoView();", selectState)
        try:
            selectState.click()
        except Exception as e:
            self.browser.execute_script("arguments[0].scrollIntoView();", selectState)
            selectState.click()
        valor='NCR'
        self.browser.find_element(By.XPATH,f'//*[text()="{valor}"]').click()
        self.browser.execute_script("arguments[0].scrollIntoView();", selectCity)
        time.sleep(1)
        selectCity.click()
        valor='Noida'
        self.browser.find_element(By.XPATH,f'//*[text()="{valor}"]').click()
        self.browser.execute_script("arguments[0].scrollIntoView();", buttonSubmit)
        buttonSubmit.click()
        
    def test_04_check_title_success(self):
        titleSuccess=self.browser.find_element(By.ID,"example-modal-sizes-title-lg")
        self.wait.until(EC.visibility_of(titleSuccess))
        print(titleSuccess.text)

    @classmethod

    def tearDownClass(inst):

       inst.browser.quit()
 
if __name__ =='__main__':
        try:
            unittest.main(verbosity=4)
        except SystemExit:
            pass