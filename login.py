# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:03:12 2020

@author: user
"""
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

url = 'https://www.dsm-dms.com'
driver = webdriver.Chrome()
driver.get(url)

delay = 3
al = Alert(driver)

driver.implicitly_wait(delay)

driver.find_element_by_xpath('//*[@id="meal"]/div/header/nav/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/input[1]').send_keys('sleepanda4523')
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/input[2]').send_keys('juhong9227#')

driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[1]/button').click()

time.sleep(1)
al.accept()

driver.find_element_by_xpath('//*[@id="apply"]/div/div[2]/a[1]/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[6]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/table/tr[4]/td[1]').click()


while True :
    if time.strftime('%H-%M-%S', time.localtime(time.time())) == '15-30-00' :
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[6]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/table/tr[4]/td[1]').click()
        
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        al.accept()
        break
    driver.implicitly_wait(1)




