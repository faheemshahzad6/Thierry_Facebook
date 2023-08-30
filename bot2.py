from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import openpyxl
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('debuggerAddress', 'localhost:9233')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
script_directory = os.path.dirname(os.path.abspath(__file__))
wait_time = 10
wait = WebDriverWait(driver, wait_time)
csv_file = os.path.join(os.path.dirname(__file__), "data.csv")
processed_rows_file = os.path.join(script_directory, "processed_rows.txt")
processed_rows = []
try:
    with open(processed_rows_file, "r") as processed_file:
        processed_rows = [int(row.strip()) for row in processed_file.readlines()]
except FileNotFoundError:
    with open(processed_rows_file, "w") as new_file:
        pass
with open(csv_file, "r", encoding="utf-8", errors="replace") as file:
    reader = csv.reader(file)
    next(reader) 
    for i, row in enumerate(reader, start=1):
        if len(row) < 2:
            continue
        if i in processed_rows:
            continue 
        title = row[0]
        url = row[1]
        
        processed_rows.append(i)
        with open(processed_rows_file, "w") as processed_file:
            processed_file.write("\n".join(str(row) for row in processed_rows))
        if url.endswith("/"):
            urld = url + "?sk=about"
        else:
            urld = url + "/?sk=about"
        driver.get(url)
        time.sleep(2)
        max_attempts = 5
        current_attempt = 1

        while current_attempt <= max_attempts:
            try:
                close_button = driver.find_element(By.XPATH, '//div[@aria-label="Close"]')
                close_button.click()
                wait = WebDriverWait(driver, 3)
                wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@aria-label="Close"]')))
                break 
            except NoSuchElementException:
                break 
            except:
                pass 
            current_attempt += 1
        try:
            about = driver.find_element(By.XPATH, '(//*[text()="About"])[1]')
            scroll_script = "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});"
            driver.execute_script(scroll_script, about)
            click_script = "arguments[0].click();"
            driver.execute_script(click_script, about)
        except:
            pass
        driver.implicitly_wait(10)
        time.sleep(random.uniform(5, 15))
        cat = "-"
        try:
            try:
                cat = driver.find_element(By.XPATH, '//span[normalize-space(text())="Categories"]/../../../..').text
                cat = cat.replace("Categories", '')
            except NoSuchElementException:
                cat = driver.find_element(By.XPATH, '//span[normalize-space(text())="Category"]/../../../..').text
                cat = cat.replace("Category", '')
            cat = cat.replace("\n", '')
        except:
            pass
        print(cat)
        driver.implicitly_wait(5)
        try:
            time.sleep(2)
            link = driver.find_elements(By.XPATH, '(//span[./a[@role="link" and @target="_blank" and not(contains(text(), "@")) and (contains(text(), "."))]])[1]')
            links = len(link)
            if links != 0:
                driver.back()
                print("This Page Have A Website Skipping it")
                continue
            
            
        except:
            pass
        email = "-"
        try:
            email = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "@") and contains(text(), ".")]')))
            #driver.find_element(By.XPATH, '//span[contains(text(), "@") and contains(text(), ".")]').text
            email = email.text
            print(email)
        except:
            pass
        address = "-"
        try:
            adds = wait.until(EC.presence_of_element_located((By.XPATH, '//span[normalize-space(text())="Address"]/../../../..')))
            input_text = adds.text
            words = input_text.split()
            if words[-1] == "Address":
                words.pop()
            address = ' '.join(words)
            print(address)
        except:
            try:
                address = driver.find_element(By.XPATH, '//a[@rel="nofollow noreferrer" and not(contains(@rel, "@"))]').text
            except:
                pass
                
            pass
            
        
        time.sleep(random.uniform(5, 15))
        driver.back()
        time.sleep(2)
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        excel_file_path = os.path.join(os.path.dirname(__file__), "Results.xlsx")
        if not os.path.exists(excel_file_path):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Name", "Email", "URL", "Category", "Address"])
        else:
            workbook = openpyxl.load_workbook(excel_file_path)
            sheet = workbook.active
        sheet.append([title, email, url, cat, address])
        workbook.save(excel_file_path)
        
with open(processed_rows_file, "w") as processed_file:
    processed_file.write("\n".join(str(row) for row in processed_rows))
