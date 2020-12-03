from urllib.request import urlretrieve
from selenium import webdriver as wb
from urllib.parse import quote_plus    # korean support
from bs4 import BeautifulSoup as BS    # Essential module
from selenium import webdriver         # Google crolling
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

keyword = input("Input keyword: ")
cnt = input("Input counter: ")
i_URL = f'https://www.google.com/search?q={quote_plus(keyword)}&sxsrf=ALeKk00OQamJ34t56QSInnMzwcC5gC344w:1594968011157&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjXs-7t1tPqAhVF7GEKHfM4DqsQ_AUoAXoECBoQAw&biw=1536&bih=754'

driver = wb.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(i_URL)
for i in range(500):
    driver.execute_script("window.scrollBy(0, 10000)")

html = driver.page_source
soup = BS(html,features="html.parser")

img = soup.select('img')

i_list = []
count = 1

print("Searching...")
for i in img:
   try:
      i_list.append(i.attrs["src"])
   except KeyError:
      i_list.append(i.attrs["data-src"])

print("Downloading...")
createFolder("images/" + keyword)
for i in i_list:
   urlretrieve(i, "images/" + keyword + "/" + keyword + "_" + str(count) + ".jpg")
   if(count == int(cnt)):
       break
   else:
       count+=1

driver.close()
print("FINISH")