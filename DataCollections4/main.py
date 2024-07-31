import time
import webbrowser
import pyautogui
from pyautogui import hotkey, click, typewrite, displayMousePosition
import csv

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
    webbrowser.open_new('https://sos.oregon.gov/business/Pages/default.aspx')
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
        
        # Click on specific coordinates 
        click(60, 75)
        time.sleep(3)
        click(697,800)
    #Click to close or navigate away 
    click(1030, 20)

# Run the test function
test1()
