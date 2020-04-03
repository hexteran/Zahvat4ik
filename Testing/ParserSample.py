import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Buffer\\chromedriver_win32\\chromedriver.exe')
driver.get('https://global.bittrex.com/Market/Index?MarketName=USD-BTC');
time.sleep(10) 
string = driver.page_source

strings = []
for i in range(1,5):
    strings.append(driver.find_element_by_xpath("//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div["+str(i)+"]"))

elements = []
for i in range(0,len(strings)):
    query1 = "//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div["+str(i+1)+"]/div[1]"
    query2 = "//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div["+str(i+1)+"]/div[2]"
    query3 = "//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div["+str(i+1)+"]/div[3]"
    elements.append([strings[i].find_element_by_xpath(query1),strings[i].find_element_by_xpath(query2),strings[i].find_element_by_xpath(query3)])

def extract(stre):
    i = stre[6:].find('>')
    j = i + stre[i:].find('<')
    return(stre[i+2+5:j])


from datetime import datetime

file = open("C:\Buffer\\chromedriver_win32\\log.txt", 'w')

for j in range(0,10):
    time.sleep(0.2) 
    file.write(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")+' :\n')
    print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")+' :\n')
    for i in elements:
        file.write("\t"+extract(i[0].get_attribute('innerHTML'))+"\t"+extract(i[1].get_attribute('innerHTML'))+"\t"+extract(i[2].get_attribute('innerHTML'))+"\n")
        print ("\t"+extract(i[0].get_attribute('innerHTML'))+"\t"+extract(i[1].get_attribute('innerHTML'))+"\t"+extract(i[2].get_attribute('innerHTML'))+"\n")
        
        
   




