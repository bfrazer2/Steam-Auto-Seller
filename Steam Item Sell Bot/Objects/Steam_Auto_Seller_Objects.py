import requests
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import getpass

class LogIn:
    
    def __init__(self, driver):
        self.driver = driver
    
    def navigate(self):
        try:
            driver.get("https://steamcommunity.com/profiles/76561198278451820/inventory")
        except:
            print("Driver failed to load input link. Check internet connection & check link for validity.")
            driver.quit()
    
    def login(self):
        try:
            context_menu = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/a'))).click()
            
        except:
            print("Could not navigate to login page.")
        
        try:
            username = getpass.getpass("Username: ")
            password = getpass.getpass("Password: ")
            
            username_textbox = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input'))).send_keys(username)
            
            password_textbox = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input'))).send_keys(password)
            
            login_button = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button'))).click()
        except:
            print("Failed to login. Please check username & password for validity.")
            driver.quit()
            
        try:
            security_code = getpass.getpass("Steam Guard Code: ")
            sg_input_box = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/form/div/div[2]/div/input[1]')))
            sg_input_box.send_keys(security_code)
        except:
            print("Steam Guard Code Authentificaiton failed, please try executing software again, and be sure to input correct steam guard code.")
            drive.quit()

class Inventory:
    
    def __init__(self, driver):
        self.driver = driver
    
    def expand(self):
        elem = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[4]/div[3]/div[1]/span'))).click()
        
        for i in range(1,6):
            show_more_button = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, ('/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[6]/div/div[{}]/div[6]'.format(i))))).click()
    
    def firefox_silly_scroll(self,passed_in_object):
        
        x = passed_in_object.location['x']
        y = passed_in_object.location['y']
            
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (x,y)
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
            
        self.driver.execute_script(scroll_by_coord)
        self.driver.execute_script(scroll_nav_out_of_way)
    
    
    def filters(self, category, *filternames):
            
        for filtername in filternames:
            
            filter_name_checkbox = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID, ('tag_filter_570_2_{}_{}').format(category, filtername.lower()))))
            
            self.firefox_silly_scroll(filter_name_checkbox)
            
            sleep(1)
            webdriver.ActionChains(driver).move_to_element(filter_name_checkbox).click(filter_name_checkbox).perform()
    
    def scrollDown(self):
        body = driver.find_element(By.XPATH, '/html/body')
        body.click()
        action.send_keys(Keys.PAGE_DOWN).perform()
    
    def sell_items(self):
        x = 0
        y = 30
        page_max_text = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID, ('pagecontrol_max')))).text
        page_max = int(page_max_text)
        print(page_max)
        cur_page = 1
        pages = True
        while pages:
            cur_page +=1
            for i in range(x,y):
                try:
                    sleep(0.5)
                    item = driver.find_elements(By.CLASS_NAME, 'itemHolder')
                    desired_item = item[i]
                    self.firefox_silly_scroll(desired_item)
                    webdriver.ActionChains(driver).move_to_element(desired_item).click(desired_item).perform()
                except:
                    continue
                try:
                    sleep(1.5)
                    sell_button = WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.ID, ('es_instantsell0'))))
                    self.firefox_silly_scroll(sell_button)
                    self.driver.execute_script("arguments[0].click();", sell_button)
                except:
                    pass
                try:
                    sell_button2 = WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.ID, ('es_instantsell1'))))
                    self.firefox_silly_scroll(sell_button2)
                    self.driver.execute_script("arguments[0].click();", sell_button2)
                except:
                    pass
                try:
                    sell_button3 = WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.ID, ('es_quicksell0'))))
                    self.firefox_silly_scroll(sell_button3)
                    self.driver.execute_script("arguments[0].click();", sell_button3)
                except:
                    pass
                try:
                    sell_button4 = WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.ID, ('es_quicksell1'))))
                    self.firefox_silly_scroll(sell_button4)
                    self.driver.execute_script("arguments[0].click();", sell_button4)
                except:
                    pass
            
            if page_max == cur_page:
                pages = False
            else:
                next_page_button = WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.ID, ('pagebtn_next')))).click()
                inventory_panel = WebDriverWait(self.driver,0.5).until(expected_conditions.presence_of_element_located((By.ID, ('inventories')))).click()
                x += 29
                y += 29
            