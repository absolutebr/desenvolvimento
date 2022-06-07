
from ast import If
from msilib.schema import Patch
from socket import close
from webbrowser import get
from requests import patch
from selenium import webdriver
import time

from setuptools import Command
driver = webdriver.Firefox()
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
import socket


wait = WebDriverWait(driver, 40)


print('MENU')

cenarios = int(input('Quantos cenarios são?' ))
instituicoes = []
clientes = []
EmissaoInicio = []
EmissaoFinal = []
gerarTags = []
gerarCsv = []

for x in range(0 , cenarios):
    print('cenario', x+1)
    instituicoes.append(input('qual codigo da instuicao? '))
    clientes.append(input('qual o codigo do cliente? '))
    EmissaoInicio.append(input('Qual a data inicial de emissao? '))
    EmissaoFinal.append(input('Qual a dta final de emissao? '))
    gerarTags.append(input('Gerar tags? '))
    gerarCsv.append(input('Gerar em csv? '))
    
for i in range(0 , cenarios):

    driver.get('http://172.25.5.21/hcosta/')

    usuario = wait.until(ec.presence_of_element_located((By.NAME, 'nome')))
    usuario.send_keys('jotha.joao')
    senha = wait.until(ec.presence_of_element_located((By.NAME, 'senha')))
    senha.send_keys('Hcosta@@')

    btn_aceitar = wait.until(ec.element_to_be_clickable((By.ID, 'botao_aceitar')))
    btn_aceitar.click()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)
    relatorioCob = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#opcoes > ul:nth-child(3)')))
    time.sleep(1)
    relatorioCob.click()

    # relatorioCob = driver.find_element_by_css_selector("#opcoes > ul:nth-child(3)").click()

    relatorioCobs = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#opcoes > ul:nth-child(3) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(3) > span:nth-child(1)')))
    relatorioCobs.click()

    sistema = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#m_3_4_9_0')))
    sistema.click()

    time.sleep(3)

    driver.switch_to.frame('conteudo')

    time.sleep(3)

        
    instituicao = wait.until(ec.presence_of_element_located((By.ID, 'instituicao')))
        
    instituicao = Select(instituicao)

    instituicao.select_by_value(instituicoes[i])

    cliente = driver.find_element_by_id('cliente').find_element_by_tag_name('optgroup').find_elements_by_tag_name('option')
    
    for lista in range(len(cliente)):
        if clientes[i] in cliente[lista].get_attribute('value'):
           cliente[lista].click()
           break       

    dataEmissao = driver.find_element_by_id('data_emissao').send_keys(EmissaoInicio[i])

    dataEmissaoFinal = driver.find_element_by_id('data_emissao_final').send_keys(EmissaoFinal[i])

    if gerarTags[i] == '1':
        tags = driver.find_element_by_css_selector('#tags').click()

    if gerarCsv[i] == '1':
        csv = driver.find_element_by_css_selector('#formato_csv').click()

    botao = driver.find_element_by_css_selector('.botao_a_direita').click()

    driver.switch_to.window(driver.window_handles[-1])

    print(get_status(driver))
    

    

    

    #os.startfile(patch)
                

        # if i == 1:

        #     patch = "C:/Users/jotha.joao.NEVESCOSTA/Downloads//boletos_cobranca.xls"

        
        #     instituicao = wait.until(ec.presence_of_element_located((By.ID, 'instituicao')))
        
        #     instituicao = Select(instituicao)

        #     try:
        #             instituicao.select_by_value('31')
        #     except:
        #             pass

        #     cliente = Select(driver.find_element_by_id('cliente'))

        #     cliente.select_by_value('436001_J_31')

        #     time.sleep(2)
        #     tags = driver.find_element_by_css_selector('#tags')

        #     tags.click()

        #     botao = driver.find_element_by_css_selector('.botao_a_direita')

        #     botao.click()


        #     while (os.startfile(patch)):
                
        #         continue        


        # if i == 2:

        #     patch = "C:/Users/jotha.joao.NEVESCOSTA/Downloads/relatorio_boletos_cobranca(1).csv"

        #     instituicao1 = wait.until(ec.presence_of_element_located((By.ID, 'instituicao')))

        #     instituicao1 = Select(instituicao1)

        #     instituicao1.select_by_value('31')

        #     select = Select(driver.find_element_by_id('cliente'))

        #     try:   
        #         select.select_by_value('436001_J_31')
        #     except: 
        #         pass
            
        #     time.sleep(2)
        #     tags = driver.find_element_by_css_selector('#tags')

        #     tags.click()

        #     csv = driver.find_element_by_css_selector('#formato_csv')

        #     time.sleep(5)

        #     csv.click()

        #     botao = driver.find_element_by_css_selector('.botao_a_direita')

        #     botao.click()

        #     time.sleep(15)

        #     os.startfile(patch)
