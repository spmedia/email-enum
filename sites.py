from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

def quitSelenium():
    driver.quit()

def mozCheck(email):
    driver.get("https://moz.com/lost-password")
    assert "Reset" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("data[User][email]")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Submit"]').click()
    sleep(1.5)
    if "That user was" in driver.page_source:
        result = "Not found"
        return result
    if "Instructions to reset" in driver.page_source:
        result = "Found"
        return result
    if "That email address appears to be invalid." in driver.page_source:
        result = "Email address invalid"
        return result
    if "Please wait 10 minutes before sending another password reset email." in driver.page_source:
        result = "Exceeded maximum tries, try again later"
        return result
    else:
        print("Captcha encountered, you'll have to check this manually")

def twitterCheck(email):
    driver.get("https://twitter.com/account/begin_password_reset")
    assert "Password Reset" in driver.title
    sleep(1)
    user = driver.find_element_by_name("account_identifier")
    user.send_keys(email)
    driver.find_element_by_class_name("EdgeButton--primary").click()
    sleep(1)
    if "We couldn't find your account with that information" in driver.page_source:
        result = "Not Found"
        return result
    if "Enter your email, phone number, or username" not in driver.page_source and "You've exceeded the number of attempts. Please try again later" not in driver.page_source:
        result = "Found"
        return result
    if "You've exceeded the number of attempts. Please try again later" in driver.page_source:
        result = "Exceeded maximum tries, try again later"
        return result
    else:
        result = "Capthca encountered, you'll have to check this manually"
        return result

def opencartCheck(email):
    driver.get("https://www.opencart.com/index.php?route=account/forgotten")
    assert "Forgotten" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("email")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Submit"]').click()
    sleep(1)
    if "Warning: The E-Mail Address was not found" in driver.page_source:
        result = "Not found"
        return result
    if "Success: An email with a reset link" in driver.page_source:
        result = "Found"
        return result
    if "Please wait 10 minutes before sending another password reset email." in driver.page_source:
        result = "Exceeded maximum tries, try again later"
        return result
    else:
        print("Captcha encountered, you'll have to check this manually")
