'''
Created on Aug 3, 2018

@author: narendra_v
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pyquery import PyQuery as pq
import pdb
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumPython(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        #self.url = "file:///D:/Python/working_example/project/PythonSelenium/assignment.html"
        self.url = "file:///C:/Users/narendra/Desktop/assignment/Navya_Assignment-master/Navya_Assignment-master/PythonSelenium/assignment.html"
        #response = requests.get()
        #print response.text 
        #soup = BeautifulSoup(self.url)
        #print soup.prettify(self.url)
        
    def method(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        elements = self.driver.find_elements_by_xpath('/html/body/nav/div/div')
        for i in elements:
            name_ = i.text
        assert name_ == 'Logo', " Error: Title name is mismatched "
        first = '//*[@id="myNavbarLeft"]/ul/li['
        last = ']'
        leftpannel = self.driver.find_elements_by_xpath('//*[@id="myNavbarLeft"]/ul/li')
        rightpannel = self.driver.find_elements_by_xpath('//*[@id="myNavbarRight"]/ul/li')
        '''
        for index in range(len(leftpannel)):
            left_result =  leftpannel[index].text
            print left_result
            #pdb.set_trace()
            left_result =  leftpannel[index].click()
            sleep(4)

        for index in range(len(rightpannel)):
            right_result =  rightpannel[index].text
            print right_result
            #pdb.set_trace()
            right_result =  rightpannel[index].click()
            sleep(4)
        '''
        sleep(4)
        posted = self.driver.find_elements_by_xpath('/html/body/div/div/div[2]/div/div/div/span/div/p[2]')

        #while (posted >=0)
        #JavascriptExecutor jse = (JavascriptExecutor)driver;        jse.executeScript("scroll(0, 250)");
        #self.driver.execute_script("arguments[0].scrollIntoView();", posted

        while True:
            
            # do the scrolling
            self.driver.execute_script("window.scrollTo(0, 250);")
            try:
                
                for index in range(len(posted)):
                    #pdb.set_trace()
                    print len(posted)
                    posted_result =  posted[index].text
                    #self.driver.execute_script("arguments[0].scrollIntoView(true);", posted[index])
                    posted[index].click()
                    print posted_result
            except e:
                print e

            finally:
                print "finihsed"




    
        print "finished"
        self.driver.quit()
           
        #assert result == (['Home Left', 'Profile', 'Friends', 'Contact'], " Name not matched")
        #print 'final' , resultl
                        
            
        
            
        #//*[@id="myNavbarLeft"]/ul/li[1]
        #//*[@id="myNavbarRight"]/ul
        #print elements('a').text()
        #self.driver.find_elements_by_name()
        #print len(elements)
        #for i in elements:
            
    
sp = SeleniumPython()
sp.method()
        
