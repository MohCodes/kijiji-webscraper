from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
import time

f = open("/home/cs/Documents/python/data.csv", 'w')
writer = csv.writer(f)

# selenium open page setup
service = Service(executable_path="/home/cs/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(
    "https://www.kijiji.ca/b-for-rent/gta-greater-toronto-area/c30349001l1700272")


def scrape_listings():
    listing_titles = driver.find_elements_by_xpath("//div[@class='title']")
    listing_prices = driver.find_elements_by_class_name("price")
    listing_location = driver.find_elements_by_class_name("location")
    listing_description = driver.find_elements_by_class_name("description")
    listing_date = driver.find_elements_by_class_name("date-posted")

    print(len(listing_titles), len(listing_prices),
          len(listing_location), len(listing_description), len(listing_date))

    listingsList = []
    writer.writerow(["Title", "Location", "Date", "Price", "description"])

    # ~45 listings per page

    for x in range(45):
        listing = []
        listing.extend([listing_titles[x].text, listing_location[x].text,
                        listing_date[x].text, listing_prices[x].text, listing_description[x].text])
        listingsList.append(listing)
        writer.writerow(listing)


def pages_to_scrape(pages):
    for x in range(pages):
        driver.find_element_by_xpath('//*[@title="Next"]').click()
        scrape_listings()


scrape_listings()
pages_to_scrape(3)
