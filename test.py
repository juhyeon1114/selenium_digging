##################
# Get mission & Set config
##################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
import requests

chrome_options = Options()

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0 },
    # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    "userAgent": "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G977N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36"
}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--window-size=400,800")

# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument("user-data-dir=C:\\Users\\dev\\AppData\\Local\\Google\\Chrome\\User Data\\profile2")
# chrome_options.add_argument("--incognito") #secret mode
# chrome_options.add_argument('--headless') #headless mode
# chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_experimental_option('w3c', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled") #navigator.webdriver 없애기
chrome_options.add_experimental_option("useAutomationExtension", False) # chrome extension 없애기
chrome_options.add_experimental_option(
    'excludeSwitches',
    [
        'disable-background-networking',
        'disable-client-side-phishing-detection',
        'disable-default-apps',
        'disable-hang-monitor',
        'disable-popup-blocking',
        'disable-prompt-on-repost',
        'disable-sync',
        'enable-automation',
        'enable-blink-features',
        'enable-logging',
        'no-first-run',
        'password-store',
        'test-type',
        'use-mock-keychain',
        'log-level',
        'ignore-certificate-errors'
        # 'remote-debugging-port',
    ]
)
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #automation style
driver.get('https://www.google.com/')
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# driver = webdriver.Chrome(executable_path='C:\\Users\\dev\\.wdm\\drivers\\chromedriver\\84.0.4147.30\\win32\\chromedriver.exe', options=chrome_options) #manual style
# driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options) #manual style
