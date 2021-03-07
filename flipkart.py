from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import json
import csv
import pandas as pd

my_url="https://www.flipkart.com/search?q=Tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
'''headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }'''
'''html=urlopen(my_url)
Soup=BeautifulSoup(html,'xml')
'''
driver = webdriver.Chrome(executable_path=r'C:\Users\kalya\chromedriver_win32\chromedriver.exe')
driver.get(my_url)
flipkart={"product_name":[],
     "price":[],
     "resolution":[],
     "OTT Support":[],
    "Warranty":[],
          }

product_names = driver.find_elements_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(n) > div:nth-child(n) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div._4rR01T')
prices = driver.find_elements_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div:nth-child(n) > div > div > div > a > div._3pLy-c.row > div.col.col-5-12.nlI3QM > div._3tbKJL > div > div._30jeq3._1_WHN1')
resolution=driver.find_elements_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div:nth-child(n) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div.fMghEO > ul > li:nth-child(3)')
OTT = driver.find_elements_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div:nth-child(n) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div.fMghEO > ul > li:nth-child(1)')
warranty=driver.find_elements_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(n) > div:nth-child(n) > div > div > div > a > div._3pLy-c.row > div.col.col-7-12 > div.fMghEO > ul > li:nth-child(8)')

flipkart["Warranty"]=list(map(lambda x:x.text,warranty))
flipkart["product_name"]=list(map(lambda x:x.text,product_names))
flipkart["price"]=list(map(lambda x:x.text,prices))
flipkart["resolution"]=list(map(lambda x:x.text,resolution))
flipkart["OTT Support"]=list(map(lambda x:x.text,OTT))
#json format
json_object = json.dumps(flipkart, indent = 4)
#print(json_object)
#csv file
with open('flipkart.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    for key, value in flipkart.items():
        writer.writerow([key, value])
#pandas data frame
#df = pd.DataFrame.from_dict(flipkart)
#print(df.head())
