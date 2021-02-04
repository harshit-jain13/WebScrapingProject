from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = 'C:\ProgramData\Anaconda3\chromedriver.exe'

options = webdriver.chrome.options.Options()
options.headless = False
driver = webdriver.Chrome(options=options,executable_path=chrome_path)

url = 'https://openaq.org/#/countries?_k=s4ax7q'
driver.get(url)
wait = WebDriverWait(driver,5)
driver.implicitly_wait(5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME,'card__title')))
countries = driver.find_elements_by_class_name('card__title')
list_of_countries = []
for country in countries:
    list_of_countries.append(country.text)
f= open('Countries.csv','w', newline='')
with f:
    writer = csv.writer(f)
    writer.writerow(list_of_countries)
time.sleep(2)
driver.quit()

