import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get("https://tinder.com/")
time.sleep(5)
log_in=driver.find_element(By.LINK_TEXT,"Log in")

log_in.click()
time.sleep(1)
more=driver.find_element(By.XPATH,'//*[@id="s2018968691"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
more.click()
time.sleep(1)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(1)
fb_username=driver.find_element(By.XPATH,'//*[@id="email"]')
fb_username.send_keys("YOUR email address")
fb_username.send_keys(Keys.TAB)
fb_password=driver.find_element(By.XPATH,'//*[@id="pass"]')
fb_password.send_keys("YOUR PASS")
log_in=driver.find_element(By.XPATH,'//*[@id="loginbutton"]')


log_in.click()
time.sleep(10)
driver.switch_to.window(base_window)
allow_loc=driver.find_element(By.XPATH,'//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[1]')
allow_loc.click()
time.sleep(1)
deny_notification=driver.find_element(By.XPATH,'//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[2]')
deny_notification.click()
time.sleep(1)
for _ in range(10):
    time.sleep(3)
    try:
        print("called")
        button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,  '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'))
        )


    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

time.sleep(10)

