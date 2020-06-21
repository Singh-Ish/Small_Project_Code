from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Ish\\Desktop\\smallprojects\\Small_Project_Code\\pycharm\\webdrivers\\chromedriver_win32\\chromedriver.exe") #for the chrome browser

driver.maximize_window()

driver.get("https://www.realtor.ca/")

driver.find_element_by_id('homeSearchTxt').send_keys('ottawa')
# driver.find_element_by_xpath('//span[@class="select2 select2-container select2-container--default select2-container--focus"]/span/span').send_keys('100000')
# driver.find_element_by_id('select2-ddlMaxPriceTop-container').send_keys("400000")
# driver.find_element_by_id('select2-ddlBedsTop-container').send_keys('2')
# baths = driver.find_element_by_xpath('//div[@id="BathsTop"]').send_keys('1+')
driver.find_element_by_id('homeSearchBtn').click()

#driver.quit()

