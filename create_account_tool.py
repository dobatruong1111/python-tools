from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(
    options=options,
)
driver.get("https://www.sephora.com")
wait = WebDriverWait(driver, 5)

def create_account():
    xpath = "/html/body/div[@id='modal-root']/div[1]/div[1]/div[2]/div[1]/div[1]"
    try:
        # First dialog
        # close_btn = driver.find_element(By.XPATH, f"{xpath}/button[1]")
        close_btn = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/button[1]")))
        close_btn.click()

        # Sign in dialog
        # create_account_btn = driver.find_element(By.XPATH, f"{xpath}/div[1]/button[1]")
        create_account_btn = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[1]/button[1]")))
        create_account_btn.click()

        # Create account dialog
        # mail_input = driver.find_element(By.XPATH, f"{xpath}/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]")
        mail_input = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]")))
        mail_input.clear()
        mail_input.send_keys("dobatruong1111@gmail.com")
        mail_input.send_keys(Keys.RETURN)

        # Form to create an account
        # first_name_input = driver.find_element(By.XPATH, f"{xpath}/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
        first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")))
        first_name_input.clear()
        first_name_input.send_keys("nhat")
        # last_name_input = driver.find_element(By.XPATH, f"{xpath}/div[2]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")
        last_name_input = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[2]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")))
        last_name_input.clear()
        last_name_input.send_keys("truong")
        # password_input = driver.find_element(By.XPATH, f"{xpath}/div[2]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[2]/form[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")))
        password_input.clear()
        password_input.send_keys("12345678")
        # month_select = driver.find_element(By.ID, "biRegMonth")
        month_select = wait.until(EC.presence_of_element_located((By.ID, "biRegMonth")))
        month_select.send_keys("January")
        # day_select = driver.find_element(By.ID, "biRegDay")
        day_select = wait.until(EC.presence_of_element_located((By.ID, "biRegDay")))
        day_select.send_keys(3)
        # join_btn = driver.find_element(By.XPATH, f"{xpath}/div[2]/form[1]/button[1]")
        join_btn = wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath}/div[2]/form[1]/button[1]")))
        join_btn.click()
        join_btn.submit()
        # join_btn.send_keys(Keys.RETURN)

        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.close()

if __name__ == "__main__":
	create_account()
    