import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def fetch_linkedin_data(linkedin_url): #to fetch linkedin data using link of profile
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.linkedin.com/login")
    print("👉 Login manually...")
    time.sleep(20)

    driver.get(linkedin_url)
    time.sleep(5)

    # scroll content till end
    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Extracting all text from page
    full_text = driver.find_element(By.TAG_NAME, "body").text

    driver.quit()

    return {
        "raw_text": full_text
    }


def format_profile(profile):
    return profile["raw_text"] #use raw text for profile formatting