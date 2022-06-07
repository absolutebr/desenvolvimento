from io import TextIOBase
from selenium import webdriver

from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.get('https://curso-python-selenium.netlify.app/exercicio_01.html')

time.sleep(2)

titulo = browser.find_element(By.TAG_NAME, 'h1')

textos = browser.find_elements(By.TAG_NAME, 'p')

for texto in textos:
    print(texto.text)

print(f'H1 {titulo.text}')