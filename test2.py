from random import randrange
from pprint import pprint
channel_id = "%032x" % randrange(16**32)

from subprocess import Popen
# HERE YOU PASS ONLY THOSE PARAMETERS YOU WANT (i.e. without --disable-*)
# BUT YOU MAY NEED --dom-automation FOR SOME ROUTINES

PATH_TO_CHROME_EXE = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
PATH_TO_CHROMEDRIVER = "C:\\Users\\dev\\.wdm\\drivers\\chromedriver\\84.0.4147.30\\win32\\chromedriver.exe"

chrome = Popen(" ".join([
    PATH_TO_CHROME_EXE,
    "--no-first-run", "--dom-automation",
    ("--testing-channel=\"NamedTestingInterface:%s\"" % channel_id),
]))

pprint(chrome)

# chrome = Popen(PATH_TO_CHROME_EXE+' '+'C:\\Users\\dev\\AppData\\Local\\Google\\Chrome\\User Data\\profile2')
# chrome = Popen(PATH_TO_CHROME_EXE)


from selenium.webdriver.chrome.service import Service
chromedriver_server = Service(PATH_TO_CHROMEDRIVER, 0)
chromedriver_server.start()
from selenium.webdriver import Remote
driver = Remote(chromedriver_server.service_url,
    {"chrome.channel": channel_id, "chrome.noWebsiteTestingDefaults": True})

driver.get('https://www.google.com/')
