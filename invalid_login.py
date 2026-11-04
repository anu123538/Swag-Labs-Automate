import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def invalid_login():
    # Create Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--disable-save-password-bubble")
    
    # Chrome driver open
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    try:
        # Navigate to website
        driver.get("https://www.saucedemo.com")
        
        # Add Login details 
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Verify that error message
        error_banner = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        
        # Check if the correct error message is displayed
        assert "Epic sadface: Sorry, this user has been locked out." in error_banner.text
        print("Locked-out user error message verified successfully!")
        
    finally:
        # Browser close
        driver.quit()

if __name__ == "__main__":
    invalid_login()