from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.chrome.service import Service
import json
from datetime import date

with open("config.json", "r") as file:
    config = json.load(file)


email = config["email"]
password_pass = config["password"]

def booker():
    current_date = date.today()
    booking_month = current_date.month - 1
    booking_day = current_date.day + 13


    WEBSITE_URL = "http://www.bushytennispadel.ie/Booking/Grid.aspx"  


    service = Service(executable_path=r"C:\Users\gusbo\chromedriver-win32\chromedriver.exe")

   
    driver = webdriver.Chrome(service=service)  
    wait = WebDriverWait(driver, 15)

    
     

    try:
    
        driver.get(WEBSITE_URL)

        date_button = driver.find_element(By.ID, "fechaTabla")  # Update locator
        date_button.click()
        wait = WebDriverWait(driver, 15)

        xpath = f'//td[@data-month="{booking_month}" and @data-year="2025"]//a[text()="{booking_day}"]'
    
        date_element = driver.find_element(By.XPATH, xpath)


        date_element.click()

        # Step 2: Select the time with columna=2
        time_xpath = '//*[name()="rect" and @time="21:00" and @columna="2"]'
        time_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, time_xpath))
        )
        time_element.click()

        button_xpath = '//*[name()="rect" and contains(@onclick, "clickBotonPista(\'c0b739b0b1fc1b1cbcd35885b5268097d4ce4644af063442c1402aa90675fc2aa81f997d3529d9d3a16d2944a35a5be5\')")]'
        button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        button_element.click()
        wait = WebDriverWait(driver, 15)

        accept_button_xpath = '//button[contains(@class, "boton") and contains(@class, "ui-button") and span[text()="Accept terms"]]'

        accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, accept_button_xpath))
        )
        accept_button.click()
        wait = WebDriverWait(driver, 15)

        email_input_xpath = '//input[@name="ctl00$ContentPlaceHolderContenido$Login1$UserName"]'
        email_address = email

        email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, email_input_xpath))
        )
        email_input.clear()  
        email_input.send_keys(email_address)


        password_input_xpath = '//input[@name="ctl00$ContentPlaceHolderContenido$Login1$Password"]'
        password = password_pass

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, password_input_xpath))
        ) 
        password_input.send_keys(password)  

        sign_in_button_xpath = '//input[@type="submit" and @name="ctl00$ContentPlaceHolderContenido$Login1$LoginButton"]'

        sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath))
        )
        sign_in_button.click() 

        wait = WebDriverWait(driver, 15)
        checkbox_id = "ctl00_ContentPlaceHolderContenido_CheckBoxAceptoCondicionesLegales"

        checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, checkbox_id))
        )
        checkbox.click() 

        book_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolderContenido_ButtonPagoCentro"))
        )

    
        book_button.click()

        print("Booking successful!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        time.sleep(20)
        driver.quit()
    return print("ran function")


booker()


