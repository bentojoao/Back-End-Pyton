from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def busca(vl):
    val = str(vl).upper()
    dr = webdriver.Chrome()
    dr.get('https://finance.yahoo.com/')
    dr.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]').send_keys(f'{val}')
    sleep(5)
    dr.find_element(By.XPATH, '//*[@id="header-desktop-search-button"]').click()
    dr.find_element(By.XPATH, '//*[@id="quote-nav"]/ul/li[5]/a/span').click()
    sleep(5)
    dr.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
    sleep(10)
    dr.close()
