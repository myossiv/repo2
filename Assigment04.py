from selenium import webdriver
from time import sleep


#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="/Users/yossi/Downloads/chromedriver")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL + Title
driver.get("https://www.walla.co.il")
get_title = driver.title
print(get_title)
#to refresh the browser
driver.refresh()
#to close the browser
sleep(5)
#driver.close()

