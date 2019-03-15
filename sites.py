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
    sleep(3)
    user = driver.find_element_by_name("data[User][email]")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Submit"]').click()
    sleep(3)
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
    else:
        print("Captcha encountered, you'll have to check this manually")
        
def botifyCheck(email):
    driver.get("https://app.botify.com/password/reset/")
    assert "Reset" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("email")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Reset"]').click()
    sleep(1)
    if "The email was not found." in driver.page_source:
        result = "Not found"
        return result
    if "An e-mail has been sent" in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")        

def ravenCheck(email):
    driver.get("https://raven-seo-tools.com/tools/m/login/forgot_password/")
    assert "Forgot" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("username")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Reset Password"]').click()
    sleep(1)
    if "Unable to locate" in driver.page_source:
        result = "Not found"
        return result
    if "We sent an email to" in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")        
        
def screamCheck(email):
    driver.get("https://www.screamingfrog.co.uk/lostpassword/")
    assert "Lost" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("user_login")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Get New Password"]').click()
    sleep(1)
    if "ERROR: There is no user" in driver.page_source:
        result = "Not found"
        return result
    if "Check your e-mail" in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")        

def wooCheck(email):
    driver.get("https://www.woorank.com/en/login/forgot")
    assert "Forgot your" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("username_email")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Rest my password"]').click()
    sleep(1)
    if "This user does not exist" in driver.page_source:
        result = "Not found"
        return result
    if "Check your e-mail" not in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")             
        
def answerCheck(email):
    driver.get("https://answerthepublic.com/users/password/new")
    assert "AnswerThe" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("user[email]")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Send password reset instructions"]').click()
    sleep(1)
    if "1 error prohibited" in driver.page_source:
        result = "Not found"
        return result
    if "You will receive an email with instructions" in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")                     

def spyCheck(email):
    driver.get("https://www.spyfu.com/auth/forgotpassword")
    assert "Forgot" in driver.title
    sleep(1.5)
    user = driver.find_element_by_id("forgot_password_email")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Send My Password"]').click()
    sleep(1)
    if "Your new password is on its way" not in driver.page_source:
        result = "Not found"
        return result
    if "Your new password is on its way" in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")                     
        
def microCheck(email):
    driver.get("https://clients.micrositemasters.com/users/password/new")
    assert "Microsite" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("user[email]")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Send me reset password instructions"]').click()
    sleep(1)
    if "not found" in driver.page_source:
        result = "Not found"
        return result
    if "not found" not in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")            
        
def buzzsumoCheck(email):
    driver.get("https://app.buzzsumo.com/password/remind")
    assert "BuzzSumo" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("email")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Reset Password"]').click()
    sleep(1)
    if "Success! We have e-mailed your password reset link" not in driver.page_source:
        result = "Not found"
        return result
    if "Success! We have e-mailed your password reset link!" in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")             
       
def ninjaCheck(email):
    driver.get("https://app.ninjaoutreach.com/Account/ForgotPassword")
    assert "Forgot" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("Email")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Submit"]').click()
    sleep(1)
    if "Error! This email was not found" in driver.page_source:
        result = "Not found"
        return result
    if "Success! Please, check your email to reset your password." in driver.page_source:
        result = "Found"
        return result
    else:
        print("Failed. Plz manually try.")                 
