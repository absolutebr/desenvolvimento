
from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By

browser= Firefox()

def findByText(browser,tag,text):

 elementos = browser.find_elements(By.TAG_NAME, tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento


browser.get('http://selenium.dunossauro.live/aula_04_a.html')

elem = findByText(browser, 'li' , 'DuckDuckGo')