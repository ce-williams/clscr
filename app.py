from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
# urllib lets you import urls as strings and use to navigate
import urllib.request

class CraigslistScraper(object):
    def __init__(self, location, postal, max_price, radius):
        self.location = location
        self.postal = postal
        self.max_price = max_price
        self.radius = radius

        self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"

        # Opening up Firefox browser
        self.driver = webdriver.Firefox()
        self.delay = 3
    # upon opening up browser, load url contained within object
    def load_craigslist_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            # driver will wait until ID needed (searchform) is loaded
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time, try increasing delay wait")



location = "sfbay"
postal = "94201"
max_price = "500"
radius = "5"

scraper = CraigslistScraper(location, postal, max_price, radius)
scraper.load_craigslist_url()
