#import Processing
import time
from selenium import webdriver
from datetime import datetime
import cv2
class Tester:
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Buffer\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('https://global.bittrex.com/Market/Index?MarketName=USD-BTC');
        time.sleep(50) 
        string = self.driver.page_source
        self.strings = []
        self.strings.append(self.driver.find_element_by_xpath("//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/span"))
        self.strings.append(self.driver.find_element_by_xpath("//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/span"))
      #//*[@id="td-web-root"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/span
        self.strings.append(self.driver.find_element_by_xpath("//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div[2]/div/span"))
        self.strings.append(self.driver.find_element_by_xpath("//*[@id=\"td-web-root\"]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[4]/div[2]/div/span"))
     #   
       # print("a")
    def extract(self, stre):
        i = ""
        j = stre.find('<')
        return(stre[:j])
    def write(self, name):
        file = open("testing\\texts\\"+name, 'w')
        #for self.j in range(0,1):
        i = self.strings
        file.write(self.extract(i[0].get_attribute('innerHTML'))+"\n"+self.extract(i[1].get_attribute('innerHTML'))+"\n"+self.extract(i[2].get_attribute('innerHTML'))+"\n"+self.extract(i[3].get_attribute('innerHTML'))+"\n")
        file.close()
#global T = Tester()
#def Init():

def Frame_Process(pic, name, T=0):
    print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))
    #T.write(name)
    cv2.imwrite("testing\\pics\\"+name+".bmp",pic)
#Frame_Process(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"))