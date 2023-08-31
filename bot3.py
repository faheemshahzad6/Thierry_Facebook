
import pandas as pd

from get_browser import get_browser

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
import datetime
import csv
import os
import undetected_chromedriver as uc
import getpass

print('s')
file_path = "Results.xlsx"
sheet_name = "Sheet"
df = pd.read_excel(file_path, sheet_name)
print('sss')
# Step 2: Extract the values from the "URLcolumn" into a list
url_list = df["URL"].tolist()

print('s')


user_data_dir = r'C:\\Users\\th_im\\Downloads\\Facebook Page Details Scrapper\\data\\'
driver = get_browser(user_data_dir=user_data_dir, profile="Profile 4")


def wait_until_935am():
    while True:
        current_time = datetime.datetime.now().time()
        target_time = datetime.time(9, 35)  # 10 am

        if current_time >= target_time:
            print("It's 9:35 Starting the work.")
            # Replace the following line with your work logic or function call
            print("Working...")
            break


while True:
    wait_until_935am()
    # driver = uc.Chrome(use_subprocess=True, options=options)
    import pyautogui
    import random
    import time

    def read_delay_from_file(filename):
        with open(filename, 'r') as file:
            content = file.read().strip()
            min_delay, max_delay = map(int, content.split(':'))
            return min_delay, max_delay
    cx = 0
    for i in url_list:
        if cx == 40:
            break
        with open('sent.txt','r') as f:
            x = f.read()
        if i in x:
            continue
        driver.get(i)
        # driver.maximize_window()
        q = 0
        time.sleep(4)
        print(i)
        with open('sent.txt','a') as f:
            f.write(i+'\n')
        time.sleep(4)
        while True:
            try:
                
                if q == 8:
                    break
                if q != -2:
                    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div").click()
                k= 0
                while True:
                    try:
                        if k == 10:
                            k=-1
                            break
                        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p')
                        print('pp')
                        break
                    except:
                        time.sleep(1)
                        k+=1
                        continue
                if k == -1:
                    break
                k= 0
                while True:
                    try:
                        if k == 10:
                            k=-1
                            break
                        image_path = 'assets/chat.png'
                        position = pyautogui.locateOnScreen(image_path, confidence=0.8,grayscale=True)
                        if position is not None:
                            # Move the mouse to the center of the located image
                            image_center = pyautogui.center(position)
                            pyautogui.click(image_center.x, image_center.y)
                            print('clicke')
                            break
                    except:
                        time.sleep(1)
                        k+=1
                        continue
                if k == -1:
                    break
                time.sleep(3)
                with open('message.txt','r',encoding='utf-8') as f:
                    msg = f.read()
                import pyperclip
                for i in msg:
                    if i == '\n':
                        pyautogui.hotkey('shift','enter')
                    else:
                        pyperclip.copy(i)

                        # Use hotkeys to paste the content from the clipboard
                        pyautogui.hotkey('ctrl', 'v')
                        time.sleep(0.1)
                time.sleep(2)
                pyautogui.press('enter')
                while True:
                    image_path = 'assets/close.png'
                    position = pyautogui.locateOnScreen(image_path, confidence=0.7,grayscale=False)
                    if position is not None:
                        # Move the mouse to the center of the located image
                        image_center = pyautogui.center(position)
                        pyautogui.click(image_center.x, image_center.y)
                        break
                cx+=1
                filename = 'delay.txt'
                min_delay, max_delay = read_delay_from_file(filename)

                # Generate a random delay between min_delay and max_delay
                random_delay = random.randint(min_delay, max_delay)

                print(f"Waiting for {random_delay} seconds...")
                time.sleep(random_delay)
                break
                
                
            except:
                try:
                    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div').click()
                    q = -2
                    continue
                except:
                    pass
                time.sleep(1)
                q+=1
                continue

