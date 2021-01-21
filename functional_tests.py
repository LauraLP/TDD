from selenium import webdriver

browser = webdriver.Firefox()
#browser.get('http://bbc.co.uk/news')
browser.get('http://localhost:8000')
assert 'Django' in browser.title
