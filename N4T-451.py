###############################################################################################
# Copyright (c) 2019, Qualitrol Corp.
# Author: Sohini Dhar, sdhar@qualitrolcorp.com
#
# VERSION          DESCRIPTION                                              DATE
#   1.1      created for Neoptix(6.53 Firmware Version)                  11/08/2019
##############################################################################################

#This test is for Automating N4T-451:
#User should be able to verify the sub-field "Geographic coordinates" under Labels and Interfaces option in the Web Page of T/Guard-408XT Device

import Common
import time

browser_driver = Common.start()
browser_driver.maximize_window()

if Common.verifyText("Test_Login.Login.Connection Successful?", "Login Page exists?", "Username:", "Login page not loaded!") != 1:
	
		Common.admin_login()
		browser_driver.get(Common.Labels_and_Interfaces_address)
		
		#Enters System Name
		
		time.sleep(0.5)
		Geographic_coordinates = browser_driver.find_element_by_id("system_lbl_4")
		Geographic_coordinates.clear()
		Geographic_coordinates.send_keys("23.0225|72.5714")
		
		#Clicks Save
		
		time.sleep(1)
		Common.click(browser_driver.find_element_by_id("submit-label"))
		
		try:
		    browser_driver.switch_to_window(Common.click(browser_driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/button")))
		except:
		    time.sleep(1)
		
		#Checks if the changes are refelected in the Status Page
		
		time.sleep(1)
		browser_driver.get(Common.Status_address)
		time.sleep(0.5)
		Common.verifyText("Test_Labels.Labels.Location_name?","Location_name Exists?","23.0225|72.5714","Names do not exist in this page")
	
		time.sleep(1)
		browser_driver.quit()
		
Common.end_test()
print("TEST SCRIPT: " + str(__file__) + " COMPLETED")

		
