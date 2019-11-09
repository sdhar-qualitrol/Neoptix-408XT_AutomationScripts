###############################################################################################
# Copyright (c) 2019, Qualitrol Corp.
# Author: Sohini Dhar, sdhar@qualitrolcorp.com
#
# VERSION          DESCRIPTION                                              DATE
#   1.1      created for Neoptix(6.53 Firmware Version)                  11/08/2019
##############################################################################################

#This test is for Automating N4T-452:
#User should be able to configure sub-field Ethernet, that is, choose Ethernet cable types(twisted-pair/fiber optics) under Labels and Interfaces option in the Web Page of T/Guard-408XT Device

import Common
import time

browser_driver = Common.start()
browser_driver.maximize_window()

if Common.verifyText("Test_Login.Login.Connection Successful?", "Login Page exists?", "Username:", "Login page not loaded!") != 1:
	
		Common.admin_login()
		browser_driver.get(Common.Labels_and_Interfaces_address)
		
		#To Select TX under Ethernet
		
		time.sleep(0.5)
		Common.click(browser_driver.find_element_by_id("system_intf_100t"))
		
		#Click Save
		
		time.sleep(1)
		Common.click(browser_driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[4]/div[2]/div/form/div[5]/center/input"))
		
		#Check if this is reflected on Status page
		
		time.sleep(1)
		browser_driver.get(Common.Status_address)
		time.sleep(0.5)
		Interfaces = browser_driver.find_element_by_id("si_int_8_intf").get_attribute('innerHTML')
		Common.verifyEqual("Test_Ethernet.Ethernet.Intefaces?","Intefaces Exists?","100Base-TX",Interfaces,"Names do not exist in this page")
		
		#To Select FX under Ethernet
		
		time.sleep(0.5)
		Common.click(browser_driver.find_element_by_id("system_intf_100fx"))
		
		#Click Save
		
		time.sleep(1)
		Common.click(browser_driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[4]/div[2]/div/form/div[5]/center/input"))
		
		#Check if this is reflected on Status page
		
		time.sleep(1)
		browser_driver.get(Common.Status_address)
		time.sleep(0.5)
		Interfaces = browser_driver.find_element_by_id("si_int_8_intf").get_attribute('innerHTML')
		Common.verifyEqual("Test_Ethernet.Ethernet.Intefaces?","Intefaces Exists?","100Base-FX",Interfaces,"Names do not exist in this page")
		
		#To Select TXFX under Ethernet
		
		time.sleep(0.5)
		Common.click(browser_driver.find_element_by_id("system_intf_100tfx"))
		
		#Click Save
		
		time.sleep(1)
		Common.click(browser_driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[4]/div[2]/div/form/div[5]/center/input"))
		
		#Check if this is reflected on Status page
		
		time.sleep(1)
		browser_driver.get(Common.Status_address)
		time.sleep(0.5)
		Interfaces = browser_driver.find_element_by_id("si_int_8_intf").get_attribute('innerHTML')
		Common.verifyEqual("Test_Ethernet.Ethernet.Intefaces?","Intefaces Exists?","100Base-TX-FX (Dual)",Interfaces,"Names do not exist in this page")
		
		time.sleep(1)
		browser_driver.quit()
		
Common.end_test()
print("TEST SCRIPT: " + str(__file__) + " COMPLETED")