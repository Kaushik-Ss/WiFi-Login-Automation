from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import socket


# Tried using various implementions so had to import ignore warning to clearly see output
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
# To replace this part of code every find element must be upgraded to the newly published selinium syntax 

def login(usr_name,pwd):
        '''
            Login function takes in parameter
            login ( username , password )
            Parameters:
                        usr_name (str) = Username
                        pwd (str) = Password
            Returns:
                        None
        '''
        # Static url
        url='http://172.17.0.1:2280/cportal/ip/user_login.php?url=http://www.gstatic.com/generate_204'
    
        # Using selinium chromium browser
        
        # driver = webdriver.Chrome()

        # Making it headless
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)


        driver.maximize_window()  
        driver.get(url) 
    
        # All the contents of the login page are placed wihtin a frame
        driver.switch_to.frame("login_win")
    
        # Waits for min ( till the contents of the page loads , 10 seconds )
        driver.implicitly_wait(10)
    
        # Hard coded for clicking Terms and conditions checkbox as all the contents were placed in a single div so clicking it normally would cause the click to be interpreted by other elements so made a workaround to toggle the Terms and conditions checkbox
        n = 2
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB * n)
        actions.send_keys(Keys.SPACE)
        actions.perform()
    
        # For typing Username
        driver.find_element_by_css_selector("#usrname").send_keys(usr_name) 
    
        # For typing password
        driver.find_element_by_xpath("/html/body/div/div[1]/form/div[5]/table[1]/tbody/tr[2]/td/input").send_keys(pwd) 

        #Just for testing purpose time.sleep() can be removed
        time.sleep(1)


    
        ''' For clicking on submit button this can also be executed by
            1. actions.send_keys(Keys.RETURN)
            2. get element and direct click or a js click function
        '''
        m = driver.find_element_by_css_selector('#update_btn')
        actions = ActionChains(driver)
        actions.move_to_element(m).click().perform()
        print('Logged in')
    

def disConnected():
    try:
        # Reference https://stackoverflow.com/questions/20913411/test-if-an-internet-connection-is-present-in-python
        # connect to the host, tells us if the host is actually reachable
        # can also check with "1.1.1.1"
        # url ="1.1.1.1"
        url="www.google.com"
        sock = socket.create_connection((url, 80))
        if sock is not None:
            print('Already connected')
            sock.close
        return False
    except OSError:
        pass
    return True

# If false positives of connection are shown then uncomment line 94
if disConnected():
    login('20I224','20I224')

# login('20I224','20I224')


