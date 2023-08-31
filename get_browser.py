import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import getpass

os_name = platform.system()

options = webdriver.ChromeOptions()


username = getpass.getuser()


def get_browser(user_data_dir):
    # if os_name == "nt":
    # print("Running for Windows...")

    # if os.name == 'nt':  # For Windows
    # chrome_path = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/profile 1"

    # chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    # user_data_dir = r'C:\\Users\\th_im\\Downloads\\Facebook Page Details Scrapper\\data\\Default'
    user_data_dir = user_data_dir
    # user_data_dir = r"C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\"
    options.add_argument(f"--user-data-dir={user_data_dir}")

    # provide the profile name with which we want to open browser
    # options.add_argument(r'--profile-directory=Default')
    # from Screenshot import Screenshot

    # disable the AutomationControlled feature of Blink rendering engine
    options.add_argument('--disable-blink-features=AutomationControlled')

    # disable pop-up blocking
    options.add_argument('--disable-popup-blocking')

    # start the browser window in maximized mode
    options.add_argument('--start-maximized')

    # disable extensions
    options.add_argument('--disable-extensions')

    # disable sandbox mode
    options.add_argument('--no-sandbox')

    # disable shared memory usage
    options.add_argument('--disable-dev-shm-usage')

    # service = Service(chrome_path)  # Replace with the path to your Chrome WebDriver executable

    browser = webdriver.Chrome(options=options)
    return browser
