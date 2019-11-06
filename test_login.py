import Common

browser_driver = Common.start()

if Common.verifyText("Test_Login.Login.Connection Successful?", "Login Page exists?", "Username:", "Login page not loaded!") != 1:
    #Testing invalid credentials
    username = browser_driver.find_element_by_id("username")
    username.send_keys("sohini")
    password = browser_driver.find_element_by_id("pasword")
    password.send_keys("wrong")
    password.send_keys(Common.Keys.RETURN)
    
    Common.verifyText("Test_Login.Login.Invalid credentials", "Invalid credentials rejected?", "Please try again!", "Accepted invalid credentials!")
    browser_driver.quit()
    
    #Testing partially valid credentials
    browser_driver = Common.start()
    username = browser_driver.find_element_by_id("username")
    username.send_keys("sohini")
    password = browser_driver.find_element_by_id("pasword")
    password.send_keys("prapti221")
    password.send_keys(Common.Keys.RETURN)
    
    Common.verifyText("Test_Login.Login.Partially Invalid credentials", "Partially invalid credentials rejected?", "Please try again!", "Accepted partially invalid credentials!")
    browser_driver.quit()

    #Testing valid credentials
    browser_driver = Common.start()
    Common.admin_login()
    
    Common.verifyText("Test_Login.Login.Valid credentials", "Valid credentials accepted?", "System", "Rejected valid credentials!")
    browser_driver.quit()
	
Common.end_test()
print("TEST SCRIPT: " + str(__file__) + " COMPLETED")
