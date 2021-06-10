from selenium import webdriver
browser=webdriver.Edge()
browser.get('http://localhost:8888')
assert 'Django' in browser.title