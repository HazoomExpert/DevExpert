from selenium import webdriver
from selenium.webdriver.common.keys import  Keys

# 1.
# Write a program that does the following:
# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. FireFox – http://www.ynet.co.il


def walla_title():
    my_driver = webdriver.Chrome()
    my_driver.get("http://www.walla.co.il")

# 2.
# In one of the browsers you open do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you
# created in clause 1.


def ynet_title():
    my_driver.get("http://www.ynet.co.il")
    title = my_driver.title
    print(title)
    my_driver.refresh()
    if title == my_driver.title:
        print("the same name")

# 3.
# Open a few browsers, locate any element, does the
# # element has the same locators in the other browser?
# Yes, elements are the same, there is no dependency between the browser and the element's location


# 4.
# Create a test with the following:
#  Open Google Translate web page
#  Write anything in Hebrew in the text area
#  Click on translate.
def translate_from_hebrew():
    my_driver.get("https://translate.google.com/")
    my_driver.find_element_by_xpath('//*[@id="source"]').send_keys("ממרם אלופים")


# 5.
#  Open Youtube web page
#  Type a name of a song
#  Click on search.
def youtube_songe():
    my_driver.get("https://www.youtube.com/")
    my_driver.find_element_by_xpath('//*[@id="search"]').send_keys("we are the champions")
    my_driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()


# 6.
# Open Chrome browser on Google Translate website:
# Ebay!!!!
#  Find translate button with 3 different locators and
# print the WebElement you created.
def ebay_search():
    my_driver.get("https://www.ebay.com/")
    my_driver.find_element_by_xpath('//*[@id="gh-ac"]').send_keys("dildo")
    my_driver.find_element_by_xpath('//*[@id="gh-btn"]').click()
    my_driver.find_element_by_xpath('/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[3]/input').click()
    my_driver.find_element_by_id('gh-btn').click()


# 7.
# Open Chrome browser on Facebook website
# https://www.facebook.com/
#  Login into Facebook (No need to send me credentials).
def facebook_login():
    my_driver.get("https://www.facebook.com/")
    my_driver.find_element_by_xpath('//*[@id="email"]').send_keys("amir@amir.com")
    my_driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456")
    my_driver.find_element_by_xpath('//*[@id="u_0_2"]').click()


# 8.
# Open Chrome browser on any webpage.
#  Delete all cookies from browser.
#  Make sure all cookies are deleted by printing all cookies
# stored in the browser.
def clear_cookies():
    my_driver.delete_all_cookies()
    print(my_driver.get_cookies())


# 9.
# Open any browser on "Github" website.
#  https://github.com/
#  Enter “Selenium” keyword in search textfield
#  Press Enter to search (through code - of course).
def git_search():
    my_driver.get("https://github.com/")
    my_driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]').send_keys('Selenium' + Keys.ENTER)


# 10.
# Find a way to disable all extensions in
# o Chrome
# o Firefox
# o Internet Explorer.
#  Run browsers without extensions.
def disable_extenstion():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    my_driver = webdriver.Chrome(chrome_options=chrome_options)

