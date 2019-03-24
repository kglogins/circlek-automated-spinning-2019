#
# Author: Karlis Gustavs Logins
# Name of the project: Automated_spinning
# Description: With Python and Selenium package and webdriver made script for automated spinning at laimesrats.lv
#

from selenium import webdriver
import time

# This path needs to be changed depending on system you are using
webdriverLocation = '/Users/kglogins/Documents/python_exercise/automated_spinning/src/chromedriver'

browser = webdriver.Chrome(webdriverLocation)

print('Getting ready...')

time.sleep(2)

# numbers = [
#     ....,
#     ....,
#     ....
# ]

for number in numbers:

    browser.get('https://www.laimesrats.lv')

    time.sleep(2)

    input = browser.find_element_by_name('pid')
    print 'Sending keys for number:', number
    input.send_keys(number)

    time.sleep(0.5)

    checkbox = browser.find_element_by_name('permission')
    print 'Clicking agree on terms'
    checkbox.click()

    time.sleep(0.5)

    submit = browser.find_element_by_class_name('undefined')
    print 'Clicking submit'
    submit.click()

    time.sleep(3)

    spinCountLeft = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]')
    spinCountLeft = int(spinCountLeft.text)

    if spinCountLeft == 0:
        print '0 spins left'
    else:
        while spinCountLeft != 0:
            spinButton = browser.find_element_by_class_name('game-btn')
            print 'Spinning! Good luck!'
            spinButton.click()
            time.sleep(6)
            browser.get('https://www.laimesrats.lv')
            print 'Refreshing page'
            time.sleep(2)
            spinCountLeft = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]')
            spinCountLeft = int(spinCountLeft.text)
            print spinCountLeft, 'spins left'

    menuButton = browser.find_element_by_class_name('bm-menu-button')
    print 'Selecting menu'

    menuButton.click()

    time.sleep(1)

    logout = browser.find_element_by_class_name('bm-logout')
    print 'Logging out'

    logout.click()

    time.sleep(2)

print 'Script ended successfully'
