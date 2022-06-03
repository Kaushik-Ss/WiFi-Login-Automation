from selenium import webdriver                                   # For Automation
import time                                                      # For debugging mostly
from selenium.webdriver.common.keys import Keys                  # For typing the user name and password
from selenium.webdriver.common.action_chains import ActionChains # For action keys and pressing the TOS
from selenium.webdriver.chrome.options import Options            # For headless automation
import requests                                                  # For connectivity check
import subprocess                                                # For netsh command to check if it is PSG WiFi
import chromedriver_autoinstaller				 # For auto installing chromedriver
import warnings							 # Tried using various implementions so had to import ignore warning to clearly see output

warnings.filterwarnings("ignore", category=DeprecationWarning) 
# To replace this part of code every find element must be upgraded to the newly published selinium syntax 

# To auto install chrome driver
chromedriver_autoinstaller.install()

def login(usr_name,pwd):
        try:
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
                try:
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
                        # time.sleep(1)


                    
                        ''' For clicking on submit button this can also be executed by
                            1. actions.send_keys(Keys.RETURN)
                            2. get element and direct click or a js click function
                        '''
                        m = driver.find_element_by_css_selector('#update_btn')
                        actions = ActionChains(driver)
                        actions.move_to_element(m).click().perform()
                        print('Logged in')
                except:
                        print('Login page was not loaded properly') 
        except:
                print("Login page is down or website's layout has been changed")
    

def disConnected():
    try:
        # Obtained from Hardcoding the index of name from netsh command
        curr=str(subprocess.check_output("netsh wlan show interfaces"))
        # If not connected to PSG Tech WiFI
        # WARNING I have assumed that all PSG Tech WiFi connections have the syntax -- PSG BH (Block name - Room no)
        if (curr[curr.index('SSID                   : '):].split()[2].startswith('PSG')==False):
            print("Not connected to PSG Tech WiFi")
            return False
    except:
        print('WiFi turned off')
        return False
    try:
        # connect to github.com, A random website if no internet then it produces
        # ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
        # Error
        x = requests.get('https://github.com/')
        print('Already  connected')
        return False
    except:
        return True



# If false positives of connection are shown then uncomment line 103
if disConnected():
    login('20I224','20I224')

#login('20I224','20I224')

