from selenium import webdriver
import pandas as pd
import csv
import time

# Webdriver settings
chrome_path = 'C:\ProgramData\Anaconda3\chromedriver.exe'

options = webdriver.chrome.options.Options()
options.headless = False
driver = webdriver.Chrome(options=options,executable_path=chrome_path)

url = 'https://openaq.org/#/locations?parameters=pm25&_k=bmrxjw'
driver.get(url)
time.sleep(2)

# This function opens .csv file that we created at the first stage
# .csv file includes names of countries
with open('Countries.csv', newline='') as f:
    reader = csv.reader(f)
    list_of_countries = list(reader)
    list_of_countries = list_of_countries[0]
    print(list_of_countries) # printing a list of countries

# Let's create Data Frame of the country & country_url
df = pd.DataFrame(columns=['country', 'country_url'])
next_button=None
# With this function we are generating urls for each country page
for country in list_of_countries[:93]:
	try:
		path = ('//span[contains(text(),' + '\"' + country + '\"' + ')]')
		next_button = driver.find_element_by_xpath(path)
		next_button.click()
		country_url = (driver.current_url)
		next_button.click()
	except:
		
		next_button.location_once_scrolled_into_view
		next_button.click()
		time.sleep(1)
		country_url = (driver.current_url)
		next_button.click()

	d = [{'country': country, 'country_url': country_url}]
	df = df.append(d)
	# After getting urls of each country page, we are saving
	# in the Data Frame the we created above the function
	
# Printing Data Frame
print(df)

# Saving created Data Frame in .csv file which will be used
# at the third stage to get the links of the card on each
# country pages
df.to_csv('2Links_Of_Countries.csv', index=False, header=True)

# Closing web browser
time.sleep(4)
driver.quit()