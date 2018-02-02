from selenium import webdriver  #to naivate web
import requests #most downloaded package. make HTML requests. parse data
from bs4 import BeautifulSoup as soup #bs4.BeautifulSoup = soup

#1) OPEN BROWSER:
chromeDriver_path = r"C:\Users\Mahmudul\Downloads\chromedriver_win32\chromedriver.exe" 
driver = webdriver.Chrome(chromeDriver_path)  

#open page
driver.get("https://www.google.com/search?source=hp&ei=2OhsWvKLGMO4zwK58aGQDQ&q=bitcoin+to+usd&oq=&gs_l=") 

#entering my stuff
myBTC = str(0.008385640000)  	#myBTC need to be a string not a float
search_box = driver.find_element_by_id("pair_base_input") #bitcoin entering box
search_box.send_keys(myBTC) 	#ENTERING my bTC, no need to enter
myDollar = 99 					#what i put in
currentURL = driver.current_url #getting current URL
print(currentURL)
print('<br>')


r = requests.get(currentURL) #the site data is now on my PC. package the request, send the requesnt, and capture the respond in a single function: request.get()
	#print(r.content) will print all the HTML stuff. BS will help me with this
page_soup = soup(r.content, "html.parser")
print( page_soup.find_all("a"))

#text = r.text #turn it into text
#page_soup = soup(r, "html.parser") 



#get the current price
newDollar = driver.find_element_by_id("pair_targ_input")
print(newDollar.text)


