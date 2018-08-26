                                                                                                            #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 12:45:24 2018
#Facebook Account Creation.
@author: rohit
"""
from selenium import webdriver
import time

url = 'https://www.facebook.com'
Firstname = input('Please Enter First Name :\n')
Surname = input('Please Enter Last Name :\n')
MobileorEmail = str(input('Enter Mobile Number or Email Address:\n'))
ReEmail = input('Please Re Enter Email address:\n')
NewPass = input('Please enter a Password :\n')
BDay = input('Please enter a Date in DD Format:\n')
Month = input('Please enter a month in word Format Eg : Dec:\n')
Year = input ('Please enter year in 1987 format:\n')
sex = int(input('Please enter male(2) or Female(1):\n'))
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_name('firstname').send_keys(Firstname)
print('First Name Entered')
driver.find_element_by_name('lastname').send_keys(Surname)
print('Last Name Entered')
driver.find_element_by_name ('reg_email__').send_keys(MobileorEmail)
print('Email or Mobile  Entered')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
driver.find_element_by_name ('reg_email_confirmation__').send_keys(ReEmail)
print('Email ReEntered successfully')
driver.find_element_by_xpath('//*[@id="u_0_v"]').send_keys(NewPass)
print('Password Entered Successfully')
driver.find_element_by_name('birthday_day').send_keys(BDay)
print('Birth Enter Successfully')
driver.find_element_by_name('birthday_month').send_keys(Month)
print('Month Enter Successfully')
driver.find_element_by_name("birthday_year").send_keys(Year)
print ('Birth Year Entered')
print ("Start : %s" % time.ctime())
time.sleep(1)
print ("End : %s" % time.ctime())
if sex ==1:
    driver.find_element_by_xpath("//*[@type='radio' and @value='1']").click()
#driver.find_element_by_id('u_0_9').find_element_by_name('sex').click()
    print('Female Selected')
else:
    driver.find_element_by_xpath("//*[@type='radio' and @value='2']").click()
#driver.find_element_by_id('u_0_a').find_element_by_name('sex').click()
    print ('Male Selected')
driver.find_element_by_name('websubmit').click()
print('Submit')
print ("Start : %s" % time.ctime())
time.sleep(5)
print ("End : %s" % time.ctime())
'''
driver.find_element_by_xpath('//*[@aria-label = "Enter code"]')
print ('Code Reached')
print ("Start : %s" % time.ctime())
time.sleep(5)
print ("End : %s" % time.ctime())
driver.find_element_by_xpath('//*[@id="u_0_9"]/div/div[3]/div/div[1]/button')
print ('Continue Button clicked.')        
'''