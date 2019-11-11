#import required global scripts and modules
from selenium import webdriver as wd

# Setup which browser driver you want to use by editing the browser var
browser = 'chrome'
if browser == 'chrome':
    driver = wd.Chrome() # start the Chrome browser
elif browser == 'firefox':
    driver = wd.Firefox() # start the FireFox browser
else:
    driver = wd.Safari() # fallback to safari browser (only work on Mac)