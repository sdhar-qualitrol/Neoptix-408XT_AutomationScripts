###############################################################################################
# Copyright (c) 2019, Qualitrol Corp.
# Author: Sohini Dhar, sdhar@qualitrolcorp.com
#
# VERSION          DESCRIPTION                                              DATE
#   1.1      created for Neoptix(6.53 Firmware Version)                  11/08/2019
##############################################################################################

#This test is for Automating N4T-454:
#User should be able to configure details of sub-field Ethernet->100Base-FX,under Labels and Interfaces option in the Web Page of T/Guard-408XT Device

import Common
import time

browser_driver = Common.start()
browser_driver.maximize_window()

if Common.verifyText("Test_Login.Login.Connection Successful?", "Login Page exists?", "Username:", "Login page not loaded!") != 1:
	
		Common.admin_login()
		browser_driver.get(Common.Labels_and_Interfaces_address)
		
		#To Select TXFX under Ethernet (since only FX does not work)
		
		time.sleep(0.5)
		Common.click(browser_driver.find_element_by_id("system_intf_100tfx"))
		
		#To check if DHCP button works and saves it and then return back to static
		
		time.sleep(0.5)
		Common.click(browser_driver.find_element_by_id("system_int_1fx"))
		time.sleep(1)
		Common.click(browser_driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[4]/div[2]/div/form/div[5]/center/input"))
		
		time.sleep(0.5)
		Common.click(browser_driver.find_element_by_id("system_int_1fx"))
		
		#Set up IP Address
		
		time.sleep(0.5)
		ip_1 = browser_driver.find_element_by_id("system_int_ip_1fx")
		ip_1.clear()
		ip_1.send_keys("10")
		
		time.sleep(0.5)
		ip_2 = browser_driver.find_element_by_id("system_int_ip_2fx")
		ip_2.clear()
		ip_2.send_keys("0")
		
		time.sleep(0.5)
		ip_3 = browser_driver.find_element_by_id("system_int_ip_3fx")
		ip_3.clear()
		ip_3.send_keys("0")
		
		time.sleep(0.5)
		ip_4 = browser_driver.find_element_by_id("system_int_ip_4fx")
		ip_4.clear()
		ip_4.send_keys("4")
		
		#Set up Subnet Mask
		
		time.sleep(0.5)
		mask_1 = browser_driver.find_element_by_id("system_int_mask_1fx")
		mask_1.clear()
		mask_1.send_keys("255")
		
		time.sleep(0.5)
		mask_2 = browser_driver.find_element_by_id("system_int_mask_2fx")
		mask_2.clear()
		mask_2.send_keys("255")
		
		time.sleep(0.5)
		mask_3 = browser_driver.find_element_by_id("system_int_mask_3fx")
		mask_3.clear()
		mask_3.send_keys("255")
		
		time.sleep(0.5)
		mask_4 = browser_driver.find_element_by_id("system_int_mask_4fx")
		mask_4.clear()
		mask_4.send_keys("0")
		
		#Set up Gateway IP Address
		
		time.sleep(0.5)
		gw_ip_1 = browser_driver.find_element_by_id("system_int_gw_1fx")
		gw_ip_1.clear()
		gw_ip_1.send_keys("10")
		
		time.sleep(0.5)
		gw_ip_2 = browser_driver.find_element_by_id("system_int_gw_2fx")
		gw_ip_2.clear()
		gw_ip_2.send_keys("0")
		
		time.sleep(0.5)
		gw_ip_3 = browser_driver.find_element_by_id("system_int_gw_3fx")
		gw_ip_3.clear()
		gw_ip_3.send_keys("0")
		
		time.sleep(0.5)
		gw_ip_4 = browser_driver.find_element_by_id("system_int_gw_4fx")
		gw_ip_4.clear()
		gw_ip_4.send_keys("1")
		
		#Checking the MAC Address
		
		time.sleep(0.5)
		MAC = browser_driver.find_element_by_id("system_int_5").get_attribute('innerHTML')
		Common.verifyEqual("Test_Interfaces.Interfaces.MAC_Address?","MAC_Address?","00:0C:CC:CC:FF:FF",MAC,"MAC  Address does not exist in this page")
		
		#Click Save
		
		time.sleep(1)
		Common.click(browser_driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[4]/div[2]/div/form/div[5]/center/input"))
		
		#Checking this inputs on Status page
		
		time.sleep(1)
		browser_driver.get(Common.Status_address)
		
		time.sleep(0.5)
		Attribution = browser_driver.find_element_by_id("si_int_10").get_attribute('innerHTML')
		Common.verifyEqual("Test_Interfaces.Interfaces.Attribution_Mode?","Attribution_Mode?","Static",Attribution,"Attribution_Mode does not exist in this page")

		time.sleep(1)
		IP = browser_driver.find_element_by_id("si_int_11").get_attribute('innerHTML')
		Common.verifyEqual("Test_Interfaces.Interfaces.IP_Address?","IP_Address?","10.0.0.4     / 255.255.255.0",IP,"IP  Address does not exist in this page")
			
		time.sleep(1)
		MAC = browser_driver.find_element_by_id("si_int_6").get_attribute('innerHTML')
		Common.verifyEqual("Test_Interfaces.Interfaces.MAC_Address?","MAC_Address?","00:0C:CC:CC:FF:FF",MAC,"MAC  Address does not exist in this page")
		
		browser_driver.quit()

Common.end_test()
print("TEST SCRIPT: " + str(__file__) + " COMPLETED")