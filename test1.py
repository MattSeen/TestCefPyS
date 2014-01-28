from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

chromedriverLocation = ".\\resources\\chromedriver.exe"
Cef3Location = ".\\CEF3_1547\\Release\\cefclient.exe"

test_url = "http://www.python.org"

def testChrome():
	chromedriver = chromedriverLocation
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)

	driver.get(test_url)
	test(driver)


def testFirefox():
	driver = webdriver.Firefox()
	driver.get(test_url)
	test(driver)


def testCef():
	chrome_options = Options()
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument("--url=" + test_url)
	chrome_options.binary_location = Cef3Location

	chromedriver = chromedriverLocation
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
	test(driver)

def test(driver):
	assert "Python" in driver.title
	elem = driver.find_element_by_name("q")
	elem.send_keys("selenium")
	elem.send_keys(Keys.RETURN)
	assert "Google" in driver.title
	driver.close()

	print "Closed driver and finished"
	pass


if __name__ == '__main__':
	testCef()


