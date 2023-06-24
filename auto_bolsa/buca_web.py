from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


def busca(vl):
    dr = webdriver.Chrome()
    dr.get('https://finance.yahoo.com/')
    pyautogui.click(332, 196, duration=1)
    dr.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]').send_keys(f'{val}')
    pyautogui.click(589, 193, duration=1)
    pyautogui.click(430, 663, duration=1)
    pyautogui.click(1045, 683, duration=1)
    # apartir da aqui é melhor usar o pyautogui 7


    sleep(2)
    '''dr.find_element(By.XPATH, '//*[@id="header-desktop-search-button"]').click()
    dr.find_element(By.XPATH, '//*[@id="quote-nav"]/ul/li[5]/a/span').click()'''
    sleep(100)
    # os valores fica diferente para cada etf
    dr.find_element(By.CLASS_NAME, '').click()
    sleep(10)
    dr.close()

busca("DIVO11")
