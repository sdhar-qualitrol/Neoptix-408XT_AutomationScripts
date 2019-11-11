###############################################################################################
# Copyright (c) 2019, Qualitrol Corp.
# Author: Sohini Dhar, sdhar@qualitrolcorp.com
#
# VERSION          DESCRIPTION                                              DATE
#   1.1      created for Neoptix(6.53 Firmware Version)                  11/08/2019
##############################################################################################

#This test is for Automating N4T-448:
#User should be able to verify the sub-field "System Name" under Labels and Interfaces option in the Web Page of T/Guard-408XT Device

import Common
import time

browser_driver = Common.start()
browser_driver.maximize_window()

if Common.verifyText("Test_Login.Login.Connection Successful?", "Login Page exists?", "Username:", "Login page not loaded!") != 1:
	
		Common.admin_login()
		browser_driver.get(Common.Labels_and_Interfaces_address)
		
		#Enters System Name
		
		time.sleep(0.5)
		System_name = browser_driver.find_element_by_id("system_lbl_1")
		System_name.clear()
		System_name.send_keys("Qualitrol T/Guard 408XT Device")
		
		#Clicks Save
		
		time.sleep(1)
		Common.click(browser_driver.find_element_by_id("submit-label"))
		
		try:
		    browser_driver.switch_to_window(Common.click(browser_driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/button")))
		except:
		    time.sleep(1)
		
		#Checks if the changes are refelected in the T/Guard Home and Status Page
		
		time.sleep(1)
		browser_driver.get(Common.T_Guard_home_address)
		time.sleep(0.5)
		System_Name = browser_driver.find_element_by_id("system-info-1").get_attribute('innerHTML')
		Common.verifyEqual("Test_Labels.Labels.System_name?","System_name Exists?","Qualitrol T/Guard 408XT Device",System_Name,"Names do not exist in this page")
		
		time.sleep(1)
		browser_driver.get(Common.Status_address)
		time.sleep(0.5)
		System_Name = browser_driver.find_element_by_id("si_info_1").get_attribute('innerHTML')
		Common.verifyEqual("Test_Labels.Labels.System_name?","System_name Exists?","Qualitrol T/Guard 408XT Device",System_Name,"Names do not exist in this page")
	
		time.sleep(1)
		browser_driver.quit()
		
Common.end_test()
print("TEST SCRIPT: " + str(__file__) + " COMPLETED")

		
