import time
import webbrowser
import pyautogui
from pyautogui import hotkey, click, typewrite
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
    print("Opening the web page...")
    # Open the web page
    webbrowser.open_new('https://sos.oregon.gov/business/Pages/default.aspx')
    time.sleep(5)  # Wait for the page to load
    
    print("Clicking initial coordinates...")
    # Click on initial coordinates (adjust as needed)
    click(625, 410)
    time.sleep(0.3)
    
    print("Scrolling down...")
    # Scroll down
    pyautogui.scroll(-1200)
    time.sleep(1)  # Allow time for scrolling
    
    print("Clicking secondary coordinates...")
    # Click on the next coordinates (adjust as needed)
    click(667, 849)
    time.sleep(1.5)
    
    for name in names:
        print(f"Typing name: {name}")
        # Type the name and press Enter
        typewrite(name)
        hotkey('enter')
        time.sleep(1.5)
        
        print("Clicking specific coordinates...")
        # Click on specific coordinates (adjust as needed)
        click(60, 75)
        time.sleep(1.5)
        click(60, 75)
    
    print("Final click...")
    # Click to close or navigate away (adjust coordinates if necessary)
    click(1030, 20)

# Run the test function
test1()
