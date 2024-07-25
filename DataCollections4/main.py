import os
import time
import webbrowser
import pyautogui
from bs4 import BeautifulSoup
from datetime import date

# Define sources with their corresponding indices
SOURCES = (
    ("https://egov.sos.state.or.us/br/pkg_web_name_srch_inq.login", 1),
    ("https://www.atozdatabases.com/search", 2)
)

# Directory to save files
DIRECTORY = os.path.dirname(__file__)
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

def perform_web_interactions(search_string, action, file_prefix, save_name):
    """
    Automates browser interactions and saves the result.
    """
    webbrowser.open(action, 1, True)
    time.sleep(4)

    pyautogui.write(search_string, interval=0.05)
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('enter')
    time.sleep(3)

    if action == SOURCES[1][0]:  # Check if this is a scan action
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)
        pyautogui.write(search_string, interval=0.05)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(5)

    pyautogui.hotkey('ctrl', 's')
    time.sleep(0.5)

    pyautogui.moveTo(SCREEN_WIDTH / 15.36, SCREEN_HEIGHT / 21.6)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.write(DIRECTORY, interval=0.05)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)

    for _ in range(6):
        pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.write(f"{file_prefix} {save_name}", interval=0.05)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('y')
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')

def parse_html(file_name):
    """
    Parses an HTML file and extracts table data.
    """
    file_path = os.path.join(DIRECTORY, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    data = []

    for index, table in enumerate(tables, start=1):
        headers = [th.text.strip() for th in table.find_all('th')]
        rows = [
            [td.text.strip() for td in row.find_all('td')]
            for row in table.find_all('tr')[1:]
        ]
        if rows:
            data.append({'headers': headers, 'rows': rows})

    return data

def check_source(site, search, string, file_prefix):
    """
    Checks the source and saves the result.
    """
    if search:
        perform_web_interactions(string, site, file_prefix, string)
        return parse_html(f"{file_prefix} {string}.html")

def scan_source(site, search, string1, string2, file_prefix):
    """
    Scans the source and saves the result.
    """
    if search:
        perform_web_interactions(string1, site, file_prefix, string2)
        return parse_html(f"{file_prefix} {string2}.html")

# Example usage:
SEARCH = "4 daughters irish pub"
ID2 = "4 daughters irish pub"

# Perform actions with the defined sources
# result_check = check_source(SOURCES[0][0], True, SEARCH, "SEARCH 1")
# result_scan = scan_source(SOURCES[0][0], True, SEARCH, ID2, "SCAN 1")

# For testing purposes:
result_scan = scan_source(SOURCES[1][0], True, SEARCH, ID2, "SCAN 2")

# Output results
if result_scan:
    for table in result_scan:
        print("Headers:", table['headers'])
        for row in table['rows']:
            print(row)
