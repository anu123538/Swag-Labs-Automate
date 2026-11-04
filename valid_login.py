import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def login_and_checkout():
    
    # disable password manager popups
    chrome_options = Options()
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    try:
        #  Navigate to Swag Labs login page
        driver.get("https://www.saucedemo.com")
        
        # Enter valid login details
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # go inventory page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        print("Logged in successfully")
        
        # Add item to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        
        #  Click on the Cart Icon
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        #  Click the Checkout button 
        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
        print("Navigated to Checkout Information page!")
        
        # add first name, last name, and postal code
        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("siri")
        
        driver.find_element(By.ID, "last-name").send_keys("sudu")
        driver.find_element(By.ID, "postal-code").send_keys("60280")
        
        # Click  Continue button
        continue_btn = driver.find_element(By.ID, "continue")
        driver.execute_script("arguments[0].click();", continue_btn)
        
        # checkout overview page
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-step-two.html")
        )
        print("Successfully Navigated to Checkout Overview page !")
        
        # Click the Finish button
        finish_btn = driver.find_element(By.ID, "finish")
        driver.execute_script("arguments[0].click();", finish_btn)
        
        # order sucessfully completed
        success_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text
        
        assert success_header == "Thank you for your order!"
        print("Order completed successfully! ")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    login_and_checkout()