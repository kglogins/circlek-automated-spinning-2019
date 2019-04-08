#
# Author: Karlis Gustavs Logins
# Name of the project: Automated_spinning
# Description: With Python and Selenium package and webdriver made script for automated spinning at laimesrats.lv
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import platform

def main():
    pathToScript = os.path.dirname(os.path.realpath(__file__)) + '/'

    system = platform.system()

    if system == 'Windows':
        pathToScript = pathToScript.replace('/', '\\')
        pathToScript = pathToScript.replace('\\', '\\\\')
        webdriverName = 'chromedriver-win.exe'

    if system == 'Darwin':
        webdriverName = 'chromedriver-mac'

    if system == 'Linux':
        webdriverName = 'chromedriver-pi'


    webdriverLocation = pathToScript + webdriverName

    print(webdriverLocation)

    browser = webdriver.Chrome(webdriverLocation)

    wait = WebDriverWait(browser, 15)

    spacer = '------------------------------'

    print(spacer)
    print(time.strftime('%d-%m-%Y %H:%M:%S', time.gmtime()))
    print(spacer)
    print('OS: ' + system)
    print('\nGetting ready...\n')

    time.sleep(0.5)

    with open(pathToScript + 'numbers.py') as file:
        numbers = file.readlines()

    if len(numbers) != 0:
        for number in numbers:

            browser.get('https://www.laimesrats.lv')

            input = wait.until(EC.presence_of_element_located((By.NAME, 'pid')))
            print('Sending keys for number:', number.rstrip())
            input.send_keys(number.rstrip())

            time.sleep(0.5)

            checkbox = wait.until(EC.presence_of_element_located((By.NAME, 'permission')))
            print('Clicking agree on terms')
            checkbox.click()

            time.sleep(0.5)

            submit = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'undefined')))
            print('Clicking submit')

            submit.click()

            time.sleep(1)

            loader = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bm-container-loader')))
            loaderDisplay = loader.value_of_css_property('display')

            counter = 0

            while loaderDisplay == 'block':
                time.sleep(0.5)
                print('Loader is in place')
                loaderDisplay = loader.value_of_css_property('display')
                if counter == 10:
                    break
                else:
                    counter = counter + 1

            time.sleep(1)

            print('Loader is not in place')

            modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bm-container-modal')))
            modalDisplay = modal.value_of_css_property('display')

            counter = 0

            while modalDisplay == 'block':
                time.sleep(0.5)
                print('Modal is in place')
                modalDisplay = modal.value_of_css_property('display')
                if counter == 10:
                    break
                else:
                    counter = counter + 1

            print('Modal is not in place')

            spinCountLeft = wait.until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]')))
            spinCountLeft = int(spinCountLeft.text)

            if spinCountLeft == 0:
                print('0 spins left')
            else:
                while spinCountLeft != 0:
                    spinButton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'game-btn')))
                    print('Spinning! Good luck!')
                    spinButton.click()
                    time.sleep(6)
                    browser.get('https://www.laimesrats.lv')
                    print('Refreshing page')
                    time.sleep(0.5)
                    spinCountLeft = wait.until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]')))
                    spinCountLeft = int(spinCountLeft.text)
                    print(spinCountLeft, 'spins left')

            menuButton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bm-menu-button')))
            print('Selecting menu')

            menuButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bm-menu-button'))).click()

            logout = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bm-logout')))
            print('Logging out\n')

            logout = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'bm-logout'))).click()

            time.sleep(2)
    else:
        print('0 numbers entered\n')

    browser.close()

    print('Script ended successfully\n')


try:
    main()
except Exception as error:
    print('Error: ', error)
    print('\nScript ended with errors!\n')
