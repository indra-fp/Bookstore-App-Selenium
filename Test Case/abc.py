from selenium import webdriver
from selenium.webdriver.common.keys import keys #for search keys
import time

from selenium.webdriver.common.by import By   #for error handling 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support	import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://partial-tense-thrasher.anvil.app")
print(driver.title)


#search by class
search = driver.find_elements_by_class_name("search-bar") #class name
search.send_keys("test") # input string want to be search in search bar (search bar "test" string)
search.send_keys(Keys.RETURN) #press enter to search

#clear the text inside input field to make sure it's empty
search.clear()


# Give some time for the code to actually work before it close to prevent errors
try: 
	#search class result saved to main
	main = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "insertelementname")) 
	print(main.text)
	

	#finding titles inside main by tag name, save to articles
	articles = main.find_elements_by_tag_name("article")

	#from articles tag name, loop for header class name
	for article in articles:
		header = article.find_elements_by_class_name("entry-title") #classname
		print(header.text)

finally:
	driver.quit()


# the point is to get access to all elements across the webpage

#time.sleep(5) #delay 



#page navigating

# find element based on link, and click
link = driver.find_elements_by_link_text("link text here ")
link.click()

#another wait so the element is loaded before continuing the next search, can use linktext

try: 
	#search class result saved to main, and click 
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, "insert link text here"))
	element.click()

#can do this over and over to find the deepest point of multiple link clicking/ button clicking

	#driver back to back to the previous page
	driver.back()

	#driver forward is also used for navigating to forward to previous back page
except: 
	driver.quit() 