'''
iOS Native Script
'''
from datetime import datetime
from lib2to3.pgen2 import driver
import sched
import unittest
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import idb
 
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', {})

def job():
  TouchAction(driver).tap(532, 2166)
  print('tap')

 
s = sched.scheduler(time, sleep)
for i in range(50):
  print(i)
  # s.enterabs(datetime(2022, 4, 14, 9, 59, 0, 999750 + 50 * (i-1)).timestamp(), 1, job)
  # s.enterabs(datetime(2022, 4, 14, 10, 0, 0, 50 * i).timestamp(), 1, job)

s.run()
