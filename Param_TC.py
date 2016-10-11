from selenium import webdriver
from Constants import *
from Home_Page import *
from LogIn_Page import *

# Maximizes the Firefox web browser then launches the github website
driver = webdriver.Firefox()
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get(URL)

'''
A for loop that tests each of the 4 cases. An expected result will yield PASS
and unexpected result will yield FAIL. The goal is for all cases to PASS.
'''
for i in range(0, len(usernameArray)):
    # Try to login successfully
    try:
        HomePage.SignIn_Button(driver).click()
        LogInPage.Username_Box(driver).send_keys(usernameArray[i])
        LogInPage.Password_Box(driver).send_keys(passwordArray[i])
        LogInPage.LogIn_Button(driver).click()
        # Check for an element that should only exist upon successful login
        if LogInPage.LogIn_Check(driver).is_displayed() and i == 0:
            # A Successful login will pass if it is Case 1
            print(caseArray[i], end=" | PASS\n")
            HomePage.LogOut1_Button(driver).click()
            HomePage.LogOut2_Button(driver).click()
        else:
            # A Successful login will fail if it is not Case 1
            print(caseArray[i], end=" | FAIL\n")
    # Do when login fails
    except:
        # Implicitly waits 10 seconds
        Exception
        # A Failed login will pass if it is Case 2, 3, or 4
        if 0 < i <= len(usernameArray):
            print(caseArray[i], end=" | PASS\n")
        # A Failed login will fail if it is Case 1
        elif i == 0:
            print(caseArray[i], end=" | FAIL\n")
        # Reload the site until the last case is reached
        if i < len(caseArray) - 1:
            driver.get(URL)
driver.quit()
