from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
myservice = Service("drivers/chromedriver")
driver = webdriver.Chrome(
    options=options,
    service=myservice
)
driver.get("https://www.sephora.com")
wait = WebDriverWait(driver, 5)

def sign_in():
    xpath = "/html/body/div[@id='modal-root']/div[1]/div[1]/div[2]/div[1]/div[1]"
    try:
        # First dialog
        # close_btn = driver.find_element(By.XPATH, f"{xpath}/button[1]")
        close_btn = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/button[1]")))
        close_btn.click()

        # Form to sign in
        # email_input = driver.find_element(By.ID, "signin_username")
        email_input = wait.until(EC.presence_of_element_located((By.ID, "signin_username")))
        email_input.clear()
        email_input.send_keys("dobatruong_t64@hus.edu.vn")
        # email_input = driver.find_element(By.ID, "signin_password")
        password_input = wait.until(EC.presence_of_element_located((By.ID, "signin_password")))
        password_input.clear()
        password_input.send_keys("12345678")
        # submit_btn = driver.find_element(By.XPATH, f"{xpath}/div[1]/form[1]/button[1]")
        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[1]/form[1]/button[1]")))
        # submit_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-at=sign_in_button]")))
        submit_btn.click()
        # submit_btn.submit()
        time.sleep(5)

        # print(driver.title)

    except Exception as e:
        print(e)
    finally:
        driver.close()

if __name__ == "__main__":
	sign_in()
    