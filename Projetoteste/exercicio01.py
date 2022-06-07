from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lu = browser.find_element(By.TAG_NAME, 'ul')

lis = lu.find_elements(By.TAG_NAME, 'li')