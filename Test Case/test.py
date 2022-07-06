import undetected_chromedriver.v2 as uc
from time import sleep

username = 'example@gmail.com'
password ='password'

driver = uc.Chrome()

driver.delete_all_cookies()

driver.get('https://accounts.google.com/ServiceLogin')
sleep(2)

driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(2)

driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(2)

driver.get('https://gmail.com')
sleep(2)