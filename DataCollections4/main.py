import time
import webbrowser
import pyautogui
from pyautogui import hotkey, click, typewrite, displayMousePosition
import csv
import requests,bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def csv_get(file_path):
    result = []
    with open(file_path) as fileObject:
        reader_obj = csv.reader(fileObject)
        for row in reader_obj:
            result.extend(row)
    return result

names = csv_get('names.csv')

def test1():
    # Open the web page
    s = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe') #path to webdriver
    driver = webdriver.Chrome(service=s)
    driver.get('https://sos.oregon.gov/business/Pages/default.aspx')
    time.sleep(5)  # Wait for the page to load
    
    # Click on initial coordinates 
    click(625, 410)
    time.sleep(0.3)
    for name in names:
        pyautogui.scroll(-5000)
        pyautogui.scroll(1000)
        time.sleep(.5)
        click(679,506)
        # Type the name and press Enter
        typewrite(name)
        hotkey('enter')
        time.sleep(3)
        # I need it to store the link of the webpage that was opened as a variable
        time.sleep(1)
        link= driver.current_url
        print(link)
        # closing out
        click(60, 75)
        time.sleep(3)
        click(697,800)
    #Click to close or navigate away 
    click(1030, 20)

# Run the test function
test1()
