from selenium import webdriver
from time import sleep
import random


def initialize():
    # TODO: download the chromedriver from https://chromedriver.chromium.org/downloads
    browser = webdriver.Chrome('./chromedriver')
    browser.get('')  # TODO: URL to the post on Instagram you want to spam

    return browser


def login(browser, username, password):
    browser.implicitly_wait(5)
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/span/a').click()

    browser.implicitly_wait(5)
    # Username field
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
    # Password field
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
    # Login button
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button').click()

    browser.implicitly_wait(5)
    # Save login info button
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()


def comment(browser):
    # TODO: list of Instagram accounts for the bot to tag (do not include the @) or list of comments for the bot
    #       to leave
    usernames = ['', '']
    count = 0
    while True:
        try:
            count = count + 1
            num = random.randint(0, len(usernames) - 1)
            sec = random.randint(30, 90)
            print(f'Number: {count} | Wait: {sec}')

            # Comment icon button
            browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()
            # Add a comment field
            browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(
                f'@{usernames[num]}')
            # Post button
            browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()

            sleep(sec)
        except Exception:
            # Stop execution for 6 minutes
            sleep(360)
            # Click post button again
            browser.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()


if __name__ == '__main__':
    username = ''  # TODO: Instagram username
    password = ''  # TODO: Instagram password
    browser = initialize()
    login(browser, username, password)
    comment(browser)
