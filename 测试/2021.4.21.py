#-*- codeing = utf-8 -*- 
#@Time : 2021/4/21 21:21
#@Author :王小刚
#@File :2021.4.21.py
#@Software：PyCharm
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'TO-DO' in browser.title
browser.quit()
