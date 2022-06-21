# Wifi Password Scraper
ONLY WORKS ON WINDOWS  

Will scrape all passwords that are registerd on your device and it will format them into a list with dicts. It will also print out the wifi name and the password.

## How it works
When running the script this happens:  
Step 1: execute the command: ```netsh wlan show profiles``` and then scrape the wifi names from them.  
Step 2: Do for every wifi name ```netsh wlan show profiles <profile name> key=clear``` after that scrape the passwords for it  
Step 3: Format and print out the result.  
