from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def test_login_crazygames():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    senha = "AdoroTestes01"
    email = "yoxew85620@foxroids.com"
    driver.get("https://crazygames.com.br")
    ##header-login-button
    ##email
    ##time para carregar
    print("oi")
    
