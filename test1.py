'''
    A doc string that explains it all, but does it?
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import sys


CHROMEDRIVERLOCATION = ".\\resources\\chromedriver.exe"
CEF3LOCATION = ".\\CEF3_1547\\Release\\cefclient.exe"
BRACKETSLOCATION = ".\\browser\\VisuUI.exe"

TEST_URL = "http://www.python.org"


def test_chrome():
    '''
        useless docstring
    '''
    print "setting up CHROME"
    chromedriver = CHROMEDRIVERLOCATION
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    driver.get(TEST_URL)
    test(driver)


def test_firefox():
    '''
        useless docstring
    '''
    print "setting up FIREFOX"
    driver = webdriver.Firefox()
    driver.get(TEST_URL)
    test(driver)


def test_cef():
    '''
        useless docstring
    '''
    print "setting up CEF"
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--url=" + TEST_URL)
    chrome_options.binary_location = CEF3LOCATION

    chromedriver = CHROMEDRIVERLOCATION
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    test(driver)

def test_brackets():
    '''
        useless docstring
    '''
    print "setting up CEF"
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--url=" + TEST_URL)
    chrome_options.add_argument("--remote-debugging-port=" + "9234")
    chrome_options.binary_location = BRACKETSLOCATION

    chromedriver = CHROMEDRIVERLOCATION
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    test(driver)


def test(driver):
    '''
        useless docstring
    '''
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)
    assert "Google" in driver.title
    driver.close()

    print "Closed driver and finished"


if __name__ == '__main__':
    
    NUMARGUMENTS = len(sys.argv)
    BROWSER = "firefox"

    print str(sys.argv)

    if(NUMARGUMENTS == 2):
        BROWSER = sys.argv[1]
        
        if BROWSER == "firefox":
            test_firefox()
        elif BROWSER == "chrome":
            test_chrome()
        elif BROWSER == "cef":
            test_cef()
        elif BROWSER == "brackets":
            test_brackets()
        else:
            print "didn't recognise browser: " + BROWSER
    else:
        print "Called me wrong"
