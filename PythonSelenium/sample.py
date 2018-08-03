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

class SeleniumPython(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.url = "file:///D:/Python/working_example/project/PythonSelenium/assignment.html"
        #response = requests.get()
        #print response.text 
        #soup = BeautifulSoup(self.url)
        #print soup.prettify(self.url)
        
    def method(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        elements = self.driver.find_elements_by_xpath('/html/body/nav/div/div/a')
        #pdb.set_trace()+
        #print elements. tst 
        for i in elements:
            print i.text
        #print elements('a').text()
        #self.driver.find_elements_by_name()
        #print len(elements)
        #for i in elements:
            
    
sp = SeleniumPython()
sp.method()
        