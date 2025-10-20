from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def test_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        WebDriverWait(driver, 10).until(
        EC.url_contains("/logged-in-successfully")
        )

        assert "/logged-in-successfully" in driver.current_url

        success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "post-title"))
        )
        assert "Logged In Successfully" in success_message.text
        print("Login realizado com sucesso!")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()