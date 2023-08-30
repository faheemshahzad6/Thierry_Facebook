from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import os

# Define constants and file paths
SEARCH_TERM = "fleuriste"
DATA_FILE = "data.csv"
CITIES_FILE = "cities.txt"
SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, DATA_FILE)
CITIES_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, CITIES_FILE)

import undetected_chromedriver as uc
import getpass
username = getpass.getuser()
if os.name == 'nt':  # For Windows
    chrome_path = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/profile 1"
options = uc.ChromeOptions()
options.headless = False
def get_hector_profile_directory():
    # Replace 'C:\\Users\\th_im\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4'
    # with the actual path to the "Hector" profile directory.
    return r'C:\\Users\\th_im\\Downloads\\Facebook Page Details Scrapper\\data\\Default'

# Get the path to the "Hector" profile directory
hector_profile_path = get_hector_profile_directory()
options.add_argument(f"user-data-dir={hector_profile_path}")
driver = uc.Chrome(use_subprocess=True, options=options)
# Function to scroll down to the end of search results
def scroll_to_end():
    while True:
        driver.implicitly_wait(2)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)
        try:
            end_of_results = driver.find_element(By.XPATH, '//*[text()="End of results"]')
            break
        except:
            d = 10
            print(f"Scrolling Down after {d} seconds")
            time.sleep(d)

# Read cities from the file
with open(CITIES_FILE_PATH, "r") as file:
    cities = [city.strip() for city in file.readlines()]

# Iterate through each city and perform the search
for city in cities:
    url = f"https://www.facebook.com/search/pages?q={SEARCH_TERM}"
    driver.get(url)
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@placeholder="Location"]').send_keys(city)
            break
        except:
            continue

    q = 0
    while True:
        try:
            if q == 4:
                q = -1
                break
            ul = driver.find_element(By.TAG_NAME,'ul')

            break
        except:
            time.sleep(1)
            q+=1
            continue
    if q == -1:
        continue
    
    q = 0
    while True:
        try:
            if q == 4:
                q = -1
                break

            ul.find_elements(By.TAG_NAME,'li')[0].click()
            break
        except:
            time.sleep(1)
            q+=1
            continue
    if q == -1:
        
        continue
    
    while True:
        try:
            divs = driver.find_element(By.CSS_SELECTOR,"div[role='feed']")
            break
        except:
            continue
    
    driver.execute_script("window.scrollBy(0, 500);")
    q = 0
    while True:
        try:
            if q == 3:
                q = -1
                break
            pages = driver.find_elements(By.XPATH, '//a[@aria-hidden="true" and @role="presentation"]')
            num_pages = len(pages)
            if num_pages == 0:
                time.sleep(1)
                q+=1
                continue
            break
        except:
            time.sleep(2)
            
            continue
    if q == -1:
        continue
    
    for i in range(num_pages):
        page = pages[i]
        actions = ActionChains(driver)
        driver.execute_script("arguments[0].scrollIntoView(true);", page)
        url = page.get_attribute("href")
        title = page.text
        print(title)
        try:
            with open(CSV_FILE_PATH, 'a', newline='', encoding="utf-8", errors="replace") as file:
                writer = csv.writer(file)
                writer.writerow([title, url])
            print("Row inserted successfully.")

        except Exception as e:
            print(f"An error occurred while inserting a row in the CSV file: {e}")

        print("Luna will scrap next page after 3 seconds")
        time.sleep(4)
    continue

print("All Cities Are Processed")
