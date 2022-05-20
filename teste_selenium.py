import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import unittest


service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.maximize_window()
browser.implicitly_wait(10)

browser.get("https://demoqa.com/")
#Initial Page
element=browser.find_element(By.XPATH,"//*[text()='Forms']")
browser.execute_script("arguments[0].scrollIntoView();", element)
element.click()
#Forms Page
practiceFormElement=browser.find_element(By.XPATH,"//*[text()='Practice Form']")
practiceFormElement.click()
#Practice Form Page
firstNameElement=browser.find_element(By.ID,"firstName")
lastNameElement=browser.find_element(By.ID,"lastName")
txtMailElement=browser.find_element(By.ID,"userEmail")
radioBTGenderFemale=browser.find_element(By.XPATH,"//*/label[text()='Female']")
radioBTGenderMale=browser.find_element(By.XPATH,"//*/label[text()='Male']")
radioBTGenderOther=browser.find_element(By.XPATH,"//*/label[text()='Other']")
txtNumber=browser.find_element(By.ID,"userNumber")
txtSubjects=browser.find_element(By.ID,"subjectsInput")
checkBoxHobbiesSports=browser.find_element(By.XPATH,"//*/label[text()='Sports']")
checkBoxHobbiesReading=browser.find_element(By.XPATH,"//*/label[text()='Reading']")
checkBoxHobbiesMusic=browser.find_element(By.XPATH,"//*/label[text()='Music']")
txtCurrentAddress=browser.find_element(By.ID,"currentAddress")
selectState=browser.find_element(By.XPATH,"//*[text()='Select State']")
selectCity=browser.find_element(By.XPATH,"//*[text()='Select City']")
buttonSubmit=browser.find_element(By.ID,"submit")
scrlDwnELement=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/span/div")

firstNameElement.send_keys("Teste")
lastNameElement.send_keys("Teste")
txtMailElement.send_keys("teste@teste.com")
radioBTGenderMale.click()
txtNumber.send_keys("0123456789")
txtSubjects.send_keys("Teste")
browser.execute_script("arguments[0].scrollIntoView();", checkBoxHobbiesSports)
checkBoxHobbiesSports.click()
txtCurrentAddress.send_keys("Teste")
browser.execute_script("arguments[0].scrollIntoView();", scrlDwnELement)
scrlDwnELement.click()
browser.execute_script("arguments[0].scrollIntoView();", selectState)
selectState.click()
valor='NCR'
browser.find_element(By.XPATH,f'//*[text()="{valor}"]').click()
browser.execute_script("arguments[0].scrollIntoView();", selectCity)
selectCity.click()
valor='Noida'
browser.find_element(By.XPATH,f'//*[text()="{valor}"]').click()
browser.execute_script("arguments[0].scrollIntoView();", buttonSubmit)
buttonSubmit.click()
wait=WebDriverWait(browser,10)
titleSuccess=browser.find_element(By.ID,"example-modal-sizes-title-lg")
wait.until(EC.visibility_of(titleSuccess))
print(titleSuccess.text)

time.sleep(30)


