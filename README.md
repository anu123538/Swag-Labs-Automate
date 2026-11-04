# Swag Labs Automated Testing Suite

This repository contains the software test documentation and automated test scripts developed for the Swag Labs e-commerce platform (`https://www.saucedemo.com`)[cite: 1].

## Project Deliverables
1. **Automated Test Scripts (Python & Selenium):**
   * **Valid Login & E2E Checkout Flow (`valid_login.py`):** Automates user login, adding an item ("Sauce Labs Bolt T-Shirt") to the cart, navigating through the cart, completing the checkout information form, and finishing the order[cite: 1].
   * **Negative Testing / Locked-out User Flow (`invalid_login.py`):** Validates the system error message handling when attempting to log in using a locked-out user account[cite: 1].

## Tech Stack
* **Language:** Python
* **Automation Tool:** Selenium WebDriver
* **Test Runner / Assertions:** PyTest & Python standard assertions
* **Browser:** Google Chrome

## Prerequisites & Installation

Ensure you have the following installed on your local machine:
* Python (v3.x or higher)
* Google Chrome browser
* Selenium and PyTest libraries

  
1.Install the required dependencies:

 pip install selenium pytest
 
2.To run the Valid Login & Checkout E2E test

  python valid_login.py
  
3.To run the Negative Test (Locked-out user error validation):

  python invalid_login.py
  

  
