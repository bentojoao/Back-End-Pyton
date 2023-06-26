from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


def busca(vl):
    dr = webdriver.Chrome()
    dr.get('https://finance.yahoo.com/')
    pyautogui.click(332, 196, duration=1)
    pyautogui.typewrite(f'{vl}')
    pyautogui.click(589, 193, duration=1)
    pyautogui.click(430, 663, duration=15)
    for c in range(0, 6):
        pyautogui.click(1045, 683, duration=1)
    pyautogui.click(646, 660, duration=10)
    sleep(10)
    dr.close()


busca("DIVO11")
