import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys

print('cmd entry:', sys.argv)

if (len(sys.argv) < 3):
    print("necessario informa email e senha")
    sys.exit()


provas_list = list()

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

#driver = webdriver.Chrome('./chromedriver')
driver.get("https://academico.pecege.org.br/Account/Login")
print(driver.title)
user_name = driver.find_element("name", "UserName")
user_name.send_keys(sys.argv[1])

password = driver.find_element("name", "Password")
password.send_keys(sys.argv[2])
password.send_keys(Keys.RETURN)

#time.sleep(5.5)

myLink = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Calendário']")))
#myLink = driver.find_element(By.XPATH, "//a[@title='Calendário']")
myLink.click()
#driver.get("https://academico.pecege.org.br/Home/Calendar")

ir_para_mes_ano = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Ir para')]")))
ir_para_mes_ano.click()

time.sleep(5.5)

#select_mes = driver.find_element(By.XPATH, "//label[@for='M_s']//following-sibling::span//child::span//child::span[@class='k-input']")
select_mes = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='M_s']//following-sibling::span//child::span//child::span[@class='k-input']")))
#select_mes = WebDriverWait(driver,15).until(EC.element_to_be_clickable(By.XPATH,"//label[@for='M_s']//following-sibling::span//child::span//child::span[@class='k-input']"))

#select_mes = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='M_s']//following-sibling::span//child::span//child::span[@class='k-input']")))
#select_mes.click()
select_mes.send_keys(Keys.DOWN)
select_mes.send_keys(Keys.DOWN)
select_mes.send_keys(Keys.DOWN)

# //label[@for='M_s']//following-sibling::span
time.sleep(5.5)
#myLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Calendário')
back = driver.find_element(By.CLASS_NAME, 'fc-icon-left-single-arrow')
back.click()
print("avaliacoes")
#avaliacoes = driver.find_element(By.XPATH, "//span[contains(text(),'Avaliação')]")
#avaliacoes = driver.find_elements(By.XPATH, '//span[text()="Avaliação"]')
#avaliacoes = driver.find_elements(By.XPATH, "//span[contains(text(),'Avaliação de')]")




#print(element.text)
avaliacoes = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Avaliação de')]")))
print(len(avaliacoes))
print(type(avaliacoes[0]))
for avaliacao in avaliacoes:
    print(avaliacao.text)
    time.sleep(2)
    #avaliacao.click()
    driver.execute_script('arguments[0].click()', avaliacao)

    provas = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@onclick,"javascript:oldestExam")]')))
    print(len(provas))
    provas_list.append(provas[0].get_attribute('onclick'))
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

print(provas_list)

#avaliacoes[0].click()

#provas = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@onclick,"javascript:oldestExam")]')))

#print(type(provas[0]))
#print(len(provas))
#print(provas[0].get_attribute('onclick'))
#ir_para_mes_ano = driver.find_element(By.CLASS_NAME, 'fc-gotoButton-button')
#ir_para_mes_ano.click()

#label
#yearFilter = driver.find_element(By.NAME, "yearFilter")
#yearFilter.send_keys("2021")


#search_bar.clear()
#search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
time.sleep(5.5)

driver.close()