from selenium import webdriver

q = input("Enter the search query: ")
q = q.replace(' ', '')
browser = webdriver.Chrome("C:/chromedriver.exe")
body = browser.find_element_by_tag_name("body")
browser.get("https://www.google.com/search?q=" + q + "&start=")
#browser.maximize_window() #maximiza janela

browser.quit()



