from __future__ import print_function
import time
import platform
import sys
import os
import codecs
import random
import string
import argparse
from junit_xml import TestSuite
from qunit_xml import TestCase
from os.path import basename
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from inspect import currentframe, getframeinfo


#
#   allow environmentals to override default account settings
#
try:
    FACTORY_USER = os.environ['FACTORY_USER']
except:
    FACTORY_USER = 'factory'

try:
    FACTORY_PASS = os.environ['FACTORY_PASS']
except:
    FACTORY_PASS = '6872500'

try:
    ADMIN_USER = os.environ['ADMIN_USER']
except:
    ADMIN_USER = 'sohini'

try:
    ADMIN_PASS = os.environ['ADMIN_PASS']
except:
    ADMIN_PASS = 'prapti2212'

try:
    DEFAULT_IP = os.environ['DEFAULT_IP']
except:
    DEFAULT_IP = '10.75.58.233'

OUT_DIR = "./results/"
USERNAME = ADMIN_USER
PASSWORD = ADMIN_PASS
cWDriver = "./webdrivers/Windows/chromedriver.exe"
cLDriver = "./webdrivers/Linux/chromedriver"
cIEDriver = "C:\\Windows\\system32\\IEDriverServer.exe"
browser_path = "./"

parser = argparse.ArgumentParser(description='Automated Test Framework.')
parser.add_argument("-b", "--browser", action="store", default="chrome",  help="Browser to use (default: chrome)")
parser.add_argument("-a", "--ip_addr", action="store", default=DEFAULT_IP, help="IP Address of test fixture to use (default: " + DEFAULT_IP + ")" )
args = parser.parse_args()

if len(sys.argv) > 0:
    print ("================================= " + sys.argv[0] + " =================================" )

test_cases = []
driver = None

# assign values from command line or defaults
NEOPTIX_IP = args.ip_addr
ip_address = "http://"+args.ip_addr


user_management_address = ip_address+"/users.php"




def setup(args):
    #Run at the start of test scripts to take in args and apply settings
    global ip_address
    global test_flag
    
def start_IE():
    global driver
    global ip_address
    print( "InternetExplorer( ", ip_address, " )" )
    driver = webdriver.Ie(cIEDriver)
    driver.get(ip_address)
    return driver
    
def start_Chrome():
    # Starts the chromedriver, assigns it to the global variable, and returns
    # the driver 
    global driver
    global ip_address
    print( "Chrome( ", ip_address, " )" )
    if platform.system() == "Windows":
        if os.path.isfile("./webdrivers/Windows/chromedriver.exe"):
            driver = webdriver.Chrome(cWDriver)
        else:
            driver = webdriver.Firefox()
    else:
        options = webdriver.ChromeOptions();
        options.add_argument('--incognito')
        dir = '/tmp/selenium/'
        if not os.path.exists(dir):
            os.makedirs(dir)
        service = "--log-path=/tmp/selenium/Chromedriver" + str(time.ctime(time.time())) + ".log"
        driver = webdriver.Chrome(chrome_options=options, executable_path=cLDriver, service_args=["--verbose",service])

    driver.get(ip_address)
    return driver

def start_FireFox():
    # Starts the chromedriver, assigns it to the global variable, and returns
    # the driver 
    global driver
    global ip_address
    print( "Firefox( ", ip_address, " )" )

    # add path to drivers
    abspath = os.path.abspath('./webdrivers/Linux')
    sys.path.append(abspath)

    # enable the Marionette driver
    fire_caps = DesiredCapabilities.FIREFOX
    fire_caps['marionette'] = True
    fire_caps['binary'] = '/usr/lib/firefox/firefox'
    driver = webdriver.Firefox(capabilities=fire_caps) 

    # open the home page
    driver.get(ip_address)
    return driver

def start():
    if( args.browser == "firefox" ):
        return start_FireFox()
    elif( args.browser == "chrome" ):
        return start_Chrome()
    elif( args.browser == "ie" ):
        return start_IE()


# This function attempts to find an element by different criterias
# starting with id, name, value attribute, and ending up by trying to search by preceding text
def get_element(txt, tag=None):
    global driver
    
    if not (isinstance(txt, str) or isinstance(txt, basestring)):
        return txt
    
    el = None
    
    # search for any tag, if not set
    if tag == None:
        tag = "*"

    try: # by id
        el = driver.find_element_by_xpath("//"+tag+"[@id='"+str(txt)+"']")
        print ("Got by ID [",txt,"]");
    except:
        try: # by name 
            el = driver.find_element_by_xpath("//"+tag+"[@name='"+str(txt)+"']")
            print ("Got by name [",txt,"]");
        except:
            try: # by value match
                el = driver.find_element_by_xpath("//"+tag+"[@value='"+str(txt)+"']")
                print ("Got by value match [",txt,"]");
            except:
                try: # by value containing value
                    el = driver.find_element_by_xpath("//"+tag+"[contains(@value,'"+str(txt)+"')]")
                    print ("Got by value contains [",txt,"]");
                except:
                    try: # by contents exact match
                        el = driver.find_element_by_xpath("//"+tag+"[text()='"+str(txt)+"']")
                        print ("Got by xpath exact match [",txt,"]");
                    except:
                        try: # by name partial match
                            el = driver.find_element_by_xpath("//"+tag+"[contains(@name,'"+str(txt)+"')]")
                            print ("Got by partial name match [",txt,"]");
                        except:
                            try: # by class exact match
                                el = driver.find_element_by_xpath("//"+tag+"[@class='"+str(txt)+"']")
                                print ("Got by class [",txt,"]");
                            except:
                                try: # by containing txt
                                    el = driver.find_element_by_xpath("//"+tag+"[contains(text(), '"+str(txt)+"')]")
                                    print ("Got by xpath contains [",txt,"]");
                                except:
                                    try: # by xpath
                                        el = driver.find_element_by_xpath(txt)
                                        print ("Got by xpath native [",txt,"]");
                                    except:
                                        try: # <input>, that is following txt
                                            el = driver.find_element_by_xpath("//*/"+tag+"[contains(.,'"+str(txt)+"')]/../input")
                                            print ("Got by xpath contains parent has text");
                                        except:
                                            print ("Warning: cannot find element %s" % (txt))
                                            #sys.exit()
    #if el:
    #    print (el.get_attribute('innerHTML').encode('ascii', 'ignore'))

    return el



# Write txt, into the element identified by find
def write (txt, into):
    global driver
    el = get_element (into)

    try: 
        if el.tag_name == 'select':
            print ("Trying to select")
            select(el, txt)
        elif el.get_attribute('type') == 'checkbox':
            if el.is_selected(): # currently selected
                if txt == False: # but needs to be not selected
                    el.click()
            elif txt == True: # not selected, but needs to be
                el.click()
        else:
            print ("Writing `" + str(txt) + "` into " + str(into))
            el.clear()
            el.send_keys(str(txt))
    except:
        print ("Warning: Cannot write `" + str(txt) + "` into " + str(into))


# Read contents of the txt
def read (txt, tag=None):
    global driver
    el = get_element (txt, tag)

    if el.tag_name == 'select':
        sel = Select(el)
        option = sel.first_selected_option
        return option.text
        #select(el, txt)
    elif el.tag_name == 'checkbox':
        if el.is_selected():
            return True
        else:
            return False
    elif el.tag_name == 'input':
        return el.get_attribute('value')
    else:
        return el.get_attribute('innerHTML')


# Click element, identified by find
def click (el):
    global driver
    
    el_txt = el
    if isinstance(el, str) or isinstance(el, basestring):
        el = get_element (el)

    # check if we have button or input
    try: 
        if (not((el.tag_name == 'input') or (el.tag_name == 'button') or (el.tag_name == 'a')) and isinstance(el_txt, str)):
            # if not, that try to search specifically for input or button
            print ("(1) Searching for input " + el_txt)
            el = get_element (el_txt, 'input')
            if el == None:
                print ("(2) Searching for button " + el_txt)
                el = get_element (el_txt, 'button')
                if el == None:
                    print ("(3) Searching for a " + el_txt)
                    el = get_element (el_txt, 'a')
    except:
        print ("(4) Searching for input " + str(el_txt))
        el = get_element (el_txt, 'input')
        if el == None:
            print ("(5) Searching for button " + str(el_txt))
            el = get_element (el_txt, 'button')
            if el == None:
                print ("(6) Searching for a " + str(el_txt))
                el = get_element (el_txt, 'a')
        
    if el:
        print ("(7) Clicking: " + el.tag_name)
        el.click()
    else:
        print ("(8) Cannot click ["+el_txt+"]")



# Test methods
    
def pass_test(t, msg=""):
    print ("PASS")
        

def fail_test(t, msg):
    t.add_failure_info(msg, msg)
    print ("FAILED: " + msg)
        
        
def verifyText(cl_name, name, find_this_txt, my_error_msg):
    global driver
    #Creates a test case dependent on whether the text is on the page or not.
    #returns False for failure
    result = True
    
    cl_name = driver.name + "." + cl_name
    test_name = cl_name.split('.')
    class_name = test_name[0] + '.' + test_name[1] + "." + test_name[2]
    test = TestCase(test_name[-1], class_name, 0,"Expecting: " + find_this_txt)
    print ("Verifying: " + name)
        
    try:
        body = driver.find_element_by_tag_name("body")
        if find_this_txt in body.text:
            pass_test(test, find_this_txt)
            result = False
        else:
           fail_test(test, my_error_msg)
    except:
        #failed
        pass
    
    test_cases.append(test)
    return result
    
    
def verifyBoolean(cl_name, name, isPass, find_this_txt, my_error_msg):
    global driver
    #Creates a test case dependent on whether the text is on the page or not.
    #returns False for failure
    result = True
    
    cl_name = driver.name + "." + cl_name
    test_name = cl_name.split('.')
    class_name = test_name[0] + '.' + test_name[1] + "." + test_name[2]
    test = TestCase(test_name[-1], class_name, 0,"Expecting: " + str(find_this_txt))
    print (name)
        
    if isPass:
        pass_test(test, find_this_txt)
        result = False
    else:
       fail_test(test, my_error_msg)
    
    test_cases.append(test)
    return result
    
    
def verifyEqual(cl_name, name, find_this_txt, compare_to_this, my_error_msg):
    #Creates a test case dependent on whether the two text fields submitted are the same
    global driver
    #returns True for failure
    result = True
    
    cl_name = driver.name + "." + cl_name
    test_name = cl_name.split('.')

    length = len (test_name)
    if length > 3:
        length = 3

    class_name = '';
    for i in range(0, length): 
        class_name += test_name[i] + '.'

    class_name = class_name.rstrip('.')

    test = TestCase(test_name[-1], class_name, 0, "Expecting: " + find_this_txt)
    print (name)

    try:
        assert find_this_txt==compare_to_this
        pass_test(test, find_this_txt)
        result = False
    except:
        fail_test(test, my_error_msg)

    test_cases.append(test)
    
    
def verifyCheckBox(cl_name, name, web_obj_id, find_this_txt, my_error_msg):
    #Creates a test case dependent on the value of the checkbox
    global driver
    #returns True for failure
    result = True
    
    cl_name = driver.name + "." + cl_name
    test_name = cl_name.split('.')
    class_name = test_name[0] + '.' + test_name[1] + "." + test_name[2]
    test = TestCase(test_name[-1], class_name, 0,"Expecting: " + str(find_this_txt))
    print (name)
    #print driver.find_element_by_id(str(web_obj_id)).get_attribute('checked')
        
    try:
        assert str(driver.find_element_by_id(str(web_obj_id)).get_attribute('checked'))==find_this_txt
        pass_test(test, find_this_txt)
        result = False
    except:
        fail_test(test, my_error_msg)
        
    test_cases.append(test)
    
    
def verifyDivText_Percent(cl_name, name, web_obj_id, find_this_txt, my_error_msg, my_percent):
    # This is used to get values from a div and
    # checks to see if the value falls within a range defined by my_percent
    global driver
    #returns False for failure
    result = True
    
    cl_name = driver.name + "." + cl_name
    test_name = cl_name.split('.')
    class_name = test_name[0] + '.' + test_name[1] + "." + test_name[2]
    test = TestCase(test_name[-1], class_name, 0,"Expecting: " + str(find_this_txt))

    print (name)
    # Helium code # print S(web_obj_id).web_element.text

    try:
        variance = float(find_this_txt * (my_percent / 100.0))
        low_limit = float(find_this_txt - variance)
        high_limit = float(find_this_txt + variance)
        curr_value = float(driver.find_element_by_id(web_obj_id).get_attribute('innerHTML'))
        assert ((curr_value >= low_limit) & (curr_value <= high_limit))
        pass_test(test, find_this_txt)
        result = False
    except:
        fail_test(test, my_error_msg)
        
    test_cases.append(test)
    return result


def record_script_failure(cl_name):
    # This is used to record failure results from the main try except loop in the calling script
    cl_name = driver.name + "." + cl_name
    test = TestCase("cl_name", cl_name, 0,"ERROR: Calling script failed to complete!")
    fail_test(test, "ERROR: Calling script failed to complete!\n" + str(sys.exc_info()[0]))
    test_cases.append(test)
    return
    

def dump_test_results():
    global OUT_DIR
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
        
    out_file = open(OUT_DIR + os.path.splitext(basename(sys.argv[0]))[0] + "_" + driver.name + ".xml", "w")
    ts = TestSuite("Login Test Suite", test_cases)
    print (TestSuite.to_xml_string([ts]), file = out_file)


def end_test():
    global driver
    if platform.system() != 'Windows':
        kill_browser()
    dump_test_results()
    driver = None


def end_test_fatal():
    print ("Fatal error ocurred, cannot continue the test")
    end_test()
    sys.exit()


def neoptix_login(username, password):
    #Used to log in to the factory account
    global driver
    global ip_address

    if driver == None:
        driver = webdriver.Firefox()
        print ("Opening page: " + str (ip_address))
        driver.get(ip_address)
        time.sleep(0.5)
    
    failed = 5
    while failed > 0:
        try:
            print ("Logging in as " + str(username) + ", " + str(password))
            u = driver.find_element_by_name("username")
            u.send_keys(username)
            p = driver.find_element_by_name("password")
            p.send_keys(password)
            p.send_keys(Keys.RETURN)
            break
        except Exception, e:
            print ("Exception: " + str(e))
            failed -= 1
            time.sleep(1)    


def admin_login():
    neoptix_login(USERNAME, PASSWORD)
        
#Checks to see if the given element exists
def element_exists():
    global driver
        
    
def kill_browser():
    global driver
    driver.quit()
    
    
    
# Set the value of a field and returns the original value
def set_field(value, element):
    try:
        original = element.get_attribute('value')
        element.clear()
        element.send_keys(str(value))
        return original
    except Exception, e:
        print( "Exception: set_field(" + str(value) + ", " + str(element) + ")" )
        print(  str(e) )
        print
    
def get_field( element ):
    try:
        return element.get_attribute('value')
    except Exception, e:
        print( "Exception: get_field(" + str(element) + ")" )
        print(  str(e) )
        print

def select_option(value, element):
    # Set the value of a select and return the original
    original = Select(element).first_selected_option.text
    element.find_element_by_xpath(".//option[contains(text(), '"+str(value)+"')]").click()
    return original
    
    
def set_check(id, state):
    #Used to set the checkbox  by id
    try:
        check    = driver.find_element_by_id(str(id))
        original = check.is_selected()
        if state == 0:
            if check.is_selected() == True:
                check.click()
                #print "unchecking"
        else:
            if check.is_selected() == False:
                check.click()
                #print "checking"
        return original
    except Exception, e:
        print( "Exception: set_check(" + str(id) + ", " + str(state) + ")" )
        print(  str(e) )
        print

def get_check(id):
    try:
        check    = driver.find_element_by_id(str(id))
        return check.is_selected()
    except Exception, e:
        print( "Exception: get_check(" + str(id) + ")" )
        print(  str(e) )
        print

def goto_Neoptix_page(myNavbar, myPage):
    hover(Link(myNavbar))
    time.sleep ( 1 )
    click(Link(myPage))
    time.sleep( 2 )

# Wrapper function
def Button(txt):
    global driver
    el = txt
    try:
        el = get_element(txt)
    except:
        print ("Warning: Button(txt) not found")
    return el


# Wrapper function
def Link(txt):
    global driver
    el = txt
    try:
        el = driver.find_element_by_xpath("//a[contains(., '"+str(txt)+"')]")
        print ("Found link(", txt, ")!")
    except:
        print ("Warning: Link(", txt, ") not found")
    return el


# Hover over an element, which can be object, or string
def hover(el):
    global driver
    if isinstance(el, str) or isinstance(el, basestring):
        el = get_element (el)
    hover = ActionChains(driver).move_to_element(el)
    hover.perform()


# Wrapper function
def S(txt):
    el = txt
    try:
        if (txt[0] == "@") or (txt[0] == "#") or (txt[0] == "."):
            txt = txt[1:]
        el = get_element(txt)
    except:
        print ("Warning: S(", txt, ") not found")
    return el


# Finds a select element (drop-down or list), and selects an option by either text or value
def select(el, text=None, value=None):
    global driver
    
    if isinstance(el, str) or isinstance(el, basestring):
        el = get_element (el)

    select = Select(el)
    
    if text:
        try:
            print ("Selecting by exact text " + str(text) + " option")
            select.select_by_visible_text(text)
        except:
            try:
                print ("Selecting by partial text " + str(text) + " option")
                option = driver.find_element_by_xpath("//select[@name='"+el.get_attribute('name')+"']/option[contains(text(), '"+str(text)+"')]")
                option.click()
            except:
                print ("Error selecting `"+str(text)+"`, cannot find such option")

    if value:
        print ("Selecting by value " + str(value))
        select.select_by_value(value)


# Wrapper function, to provide back-capability with helium
def ComboBox(txt):
    global driver
    el = txt
    try:
        el = get_element(txt)
    except:
        print ("Warning: ComboBox(", txt, ") not found")
    return el

# Generate a @size long string string, that consists of random combination of @chars
def random_string(size=6, chars=None):
    if not chars:
        chars = string.digits + string.letters # string.printable - has bunch of characters
    return ''.join(random.choice(chars) for _ in range(size))


def find_all_by_class(txt):
    global driver
    els = driver.find_elements_by_class_name(txt)
    return els
