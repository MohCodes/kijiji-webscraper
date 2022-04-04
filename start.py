from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv
import time

f = open("/home/cs/Documents/python/data.csv", 'w')
writer = csv.writer(f)
writer.writerow(["Name", "Post Date", "Price"])


def openPage():
    service = Service(executable_path="/home/cs/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get(
        "https://www.kijiji.ca/b-for-rent/gta-greater-toronto-area/c30349001l1700272")
    time.sleep(15)

    listingID = 4

    # listingPrice = driver.find_elements_by_class_name("price").text
    # listingLocation = driver.find_elements_by_class_name("location").text
    # listingDescription = driver.find_elements_by_class_name("description").text

    for x in range(20):
        listingID = listingID+1

        if listingID == 9:
            listingID = 10

        if listingID == 14:
            listingID = 15
        if listingID == 19:
            listingID = 20

        listingsPrice = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[3]/div[3]/main/div[2]/div[{id}]/div[1]/div[2]/div/div[1]".format(id=listingID)).text
        listingTitle = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[3]/div[3]/main/div[2]/div[{idT}]/div/div[2]/div/div[2]/a".format(idT=listingID)).text
        listingDate = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[3]/div[3]/main/div[2]/div[{idD}]/div/div[2]/div/div[4]/span[2]".format(idD=listingID)).text

        content = [listingTitle, listingDate, listingsPrice]

        writer.writerow(content)

        # print(listingTitle, " ", listingPrice, " ",
        #       listingLocation, " ", listingDescription)

        # listings = driver.find_elements(By.CLASS_NAME, "info")


openPage()
