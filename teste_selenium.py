#!/usr/bin/env python

from selenium import webdriver

from datetime import datetime
from selenium.webdriver.chrome.service import Service
from  webdriver_manager.chrome import ChromeDriverManager

# cria uma nova sessao no browser
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.maximize_window()

# navega para a home page do Google

browser.get("http://www.google.com/")

# procura pelo elemento referente a searchbox

search_field = browser.find_element_by_name("q")

# envia a string @query para o element e realiza a busca

query = "Test Driven Development"

search_field.send_keys(query)

search_field.submit()

# espera até 3 segundos até o resultado ficar pronto

browser.implicitly_wait(3) 

# procura pelos resultados

results = browser.find_elements_by_class_name("r")

# para cada resultado (<div>) procura a ancora (<a>) que contem o link da pagina

print("* {} primeiros resultados para a busca ‘{}’:".format(len(results), query))

for index, r in enumerate(results):

        link = r.find_elements_by_tag_name("a")[0].get_attribute("href")

        print("\t{:2d}. {}".format(index + 1, link))

# tira um print da pagina

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

browser.save_screenshot('search_screenshot-{}.png'.format(now))

# fecha a sessao com o browser

browser.quit()