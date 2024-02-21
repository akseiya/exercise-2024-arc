#!/usr/bin/env -S pipenv run python -i

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def errout(wat):
  print(f'\n\n\n{wat}\n\n\n', file=sys.stderr, flush=True)
  sys.stderr.flush()

chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = '/usr/bin/chromium-browser'
chromeOptions.add_argument("--remote-debugging-port=9222")
# chromeOptions.add_argument("--no-sandbox")
# chromeOptions.add_argument("--disable-shm-usage")

wd = webdriver.Chrome(options=chromeOptions)

wd.get('http://google.com')
assert 'Google' in wd.title

reject = wd.find_element(By.XPATH, '//button[normalize-space()="Reject all"]')
reject.click()

wd.close()

# import pry; pry()


