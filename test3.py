from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
import requests

from random import randrange
channel_id = "%032x" % randrange(16**32)
from subprocess import Popen
chrome_options = Options()

PATH_TO_CHROME_EXE = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
PATH_TO_CHROMEDRIVER = "C:\\Users\\dev\\.wdm\\drivers\\chromedriver\\84.0.4147.30\\win32\\chromedriver.exe"

chrome = Popen(" ".join([
    PATH_TO_CHROME_EXE,
    "--no-first-run", "--dom-automation",
    ("--testing-channel=\"NamedTestingInterface:%s\"" % channel_id),
]))

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.chrome(ChromeDriverManager().install()) #automation style
