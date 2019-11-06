import Common
import time

browser_driver = Common.start()

if Common.verifyText("Test_Login.Id_Setup.Connection Successful?", "Login Page exists?", "Username:", "Login page not loaded!") != 1:
        
        time.sleep(1)
        Common.admin_login()
        
        browser_driver.maximize_window()

        time.sleep(1)
        browser_driver.get(Common.user_management_address)
		
	if Common.verifyText("Test_UserManagement.UserManagement.Invalid input", "Invalid input rejected?", "User management", "Selected page does not exist!")!= 1:
	    print("User Management is visible")
        else:
            print("Failed to Load Page")
			
	time.sleep(1)
		
        #To Add a new user as admin
	
        time.sleep(1)	
	Common.click("Add new user")
		
	Username = browser_driver.find_element_by_id("u")
	Username.send_keys("NewUser")
	
	time.sleep(0.5)
	
	Password = browser_driver.find_element_by_name("p")
	Password.send_keys("Pass")
	
	time.sleep(0.5)
	
	ConfirmPassword = browser_driver.find_element_by_name("p2")
	ConfirmPassword.send_keys("Pass")
	
	time.sleep(0.5)
	Common.click("Save")
	
	Common.verifyText("Test_UserManagement.UserManagement.NewUserAddition", "NewUserAddition rejected?", "NewUser", "Chosen User does not exist!")
	
	browser_driver.refresh()
	
	#To Add a new user as guest
	time.sleep(1)	
	Common.click("Add new user")
		
	Username = browser_driver.find_element_by_id("u")
	Username.send_keys("G_User")
	
	time.sleep(0.5)
	
	Password = browser_driver.find_element_by_name("p")
	Password.send_keys("Pass")
	
	time.sleep(0.5)
	
	ConfirmPassword = browser_driver.find_element_by_name("p2")
	ConfirmPassword.send_keys("Pass")
	
	time.sleep(0.5)
	
	Common.click(browser_driver.find_element_by_name("c"))
	Common.click("Save")
	
	Common.verifyText("Test_UserManagement.UserManagement.NewUserAddition", "NewUserAddition rejected?", "G_User", "Chosen User does not exist!")
	

	#To Delete newly added Users
	
	Common.click("NewUser")
	Common.click("Delete User")
	
	time.sleep(2)
	
	try:
	    browser_driver.switch_to_window(Common.click(browser_driver.find_element_by_xpath("//html/body/div[4]/div[3]/div/button[1]")))
	except:
		time.sleep(1)
	
	browser_driver.refresh()
	
	Common.click("G_User")
	Common.click("Delete User")
	
	time.sleep(2)
	
	try:
	    browser_driver.switch_to_window(Common.click(browser_driver.find_element_by_xpath("//html/body/div[4]/div[3]/div/button[1]")))
	except:    
		time.sleep(1)
				
		
	browser_driver.quit()		
Common.end_test()
print("TEST SCRIPT: " + str(__file__) + " COMPLETED")
