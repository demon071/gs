from selenium import webdriver
import time, json
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def exist_element(driver, by:str, value:str):
    try:
        driver.find_element(by, value)
        return True
    except WebDriverException:
        return False
def is_active_element(driver, by:str, value:str):
    active = not driver.find_element(by, value).get_attribute('disabled')
    return active
def wait_element(driver, by:str, value:str, time_out:float = 30.0, wait_enable = False, return_ele = False):
    time_old = time.time()
    while time.time()-time_old<time_out:
        if exist_element(driver, by, value):
            if not wait_enable:
                return True
            elif is_active_element(driver, by, value):
                return True
        else:
            time.sleep(0.2)
    return False

def is_element(driver, by:str, value:str, return_ele = False):
    try:
        ele = driver.find_element(by, value)
        if return_ele:
            return ele
        return True
    except WebDriverException:
        return False


options = webdriver.ChromeOptions()
# options.add_argument("--window-size=480,720")
path = str(Path().absolute())

profile = path+'\\profile'
options.add_argument('--user-data-dir='+profile)
options.set_capability('goog:loggingPrefs',{'performance': 'ALL'} )
options.binary_location = path + "\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"
chromedriver = path + '\\chromedriver.exe'
driver = webdriver.Chrome(service=ChromeService(chromedriver), options=options)

driver.get('https://www.capcut.com/editor?lang=en')

wait_element(driver, By.XPATH, '//div[@class="lv_sign_in_panel_wide-right-wrapper"]')

sign_close = driver.find_element(By.XPATH, '//*[@class="lv_sign_in_panel_wide-close"]')
sign_close.click()

# lv_sign_in_panel_wide-right-wrapper

# lv_sign_in_panel_wide-close

# //*[@id="PlaceholderUpload"]/div[1]/div[2]/input

# PlaceholderUpload = driver.find_element(By.XPATH, '//div[@id="PlaceholderUpload"]//*[@type="file"]')
# PlaceholderUpload.send_keys('D:\WORK/TEST/Capcut Sub/audio.mp3')
# setFlag = False
# while True:
#     logs_raw = driver.get_log("performance")
#     logsMain = [json.loads(lr["message"])["message"] for lr in logs_raw]
#     logs = [log for log in logsMain if (log["method"] == "Network.requestWillBeSent")]
#     logsExtra = [log for log in logsMain if (log["method"] == "Network.requestWillBeSentExtraInfo")]
#     logr = [log for log in logsMain if (log["method"] == "Network.responseReceived")]
#     for log in logr:
#         if "response" in log["params"]:
#                 if "url" in log["params"]["response"]:
#                     if '/lv/v1/upload/get_upload_task' in log["params"]["response"]["url"]:
#                         setFlag = True
#                         break
#     if setFlag:
#         break

#     time.sleep(1)

# Network.responseReceived

# https://edit-api-sg.capcut.com/lv/v1/upload/get_upload_task
cap_ele = wait_element(driver, By.XPATH, '//*[@data-ssr-i18n-value="Captions"]', time_out=2)
if cap_ele:
    captions = driver.find_element(By.XPATH, '//*[@data-ssr-i18n-value="Captions"]')
    captions.click()
elif wait_element(driver, By.XPATH, '//*[@data-ssr-i18n-value="Chú thích"]', time_out=2):
    print('None')
    captions = driver.find_element(By.XPATH, '//*[@data-ssr-i18n-value="Chú thích"]')
    captions.click()

    if wait_element(driver, By.XPATH, '//*[@id="text-intelligent-detect-text"]', time_out=2):
        print('ok1')
        detect = driver.find_element(By.XPATH, '//*[@id="text-intelligent-detect-text"]')
        detect.click()
        if wait_element(driver, By.XPATH, '//*[@id="text-intelligent-detect-text"]//input', time_out=2):
            print('ok2')
            select = driver.find_element(By.XPATH, '//*[@id="text-intelligent-detect-text"]//input')
            ActionChains(driver).move_to_element(select).perform()
            ActionChains(driver).click(select).perform()
            
            # try:
            # #     select.click()
            #     select.send_keys('US')
            # except:
            #     import traceback
            #     print(traceback.format_exc())
            # select.click()
            # select.send_keys('US')
            # if wait_element(driver, By.XPATH, '//*[@id="text-intelligent-detect-text"]//button', time_out=10):
            #     button = driver.find_element(By.XPATH, '//*[@id="text-intelligent-detect-text"]//button')
            #     button.click()
            #     setFlag = False
            #     while True:
            #         logs_raw = driver.get_log("performance")
            #         logsMain = [json.loads(lr["message"])["message"] for lr in logs_raw]
            #         logs = [log for log in logsMain if (log["method"] == "Network.requestWillBeSent")]
            #         logsExtra = [log for log in logsMain if (log["method"] == "Network.requestWillBeSentExtraInfo")]
            #         logr = [log for log in logsMain if (log["method"] == "Network.responseReceived")]
            #         for log in logr:
            #             if "response" in log["params"]:
            #                     if "url" in log["params"]["response"]:
            #                         if '/v1/caption/query' in log["params"]["response"]["url"]:
            #                             print(json.dumps(log, indent=4))
            #                             try:
            #                                 body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
            #                                 print(body)
            #                             except:
            #                                 print('err')
            #                             setFlag = True
            #                             break
            #         if setFlag:
            #             break
            #         time.sleep(1)
        
        # //*[@id="text-intelligent-detect-text"]//button
    # text-intelligent-detect-text
    # Chú thích
# //*[@data-ssr-i18n-value="Captions"]
# //*[@id="lv-select-popup-1"]/div/div/li[4]
# //*[@id="lang"]/div/div/div/span/input

time.sleep(35)

driver.quit()