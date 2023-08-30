@echo off
set "chrome_path=C:\Program Files\Google\Chrome\Application\chrome.exe"
set "user_data_dir=C:\Users\th_im\Downloads\Facebook Page Details Scrapper\data"
set "custom_port=9233"
"%chrome_path%" --remote-debugging-port=%custom_port% --user-data-dir="%user_data_dir%"