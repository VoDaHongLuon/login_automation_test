from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ===============================
# 🚦 SETUP: Khởi tạo WebDriver (Firefox)
# ===============================
def setup_driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)  # Đợi tối đa 5s để tìm phần tử
    return driver

# ===============================
# 📝 TEST CASES
# ===============================
def test_login_success(driver):
    """TC_01: Đăng nhập thành công"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    assert "inventory.html" in driver.current_url
    print("✅ TC_01: login success")


def test_login_wrong_password(driver):
    """TC_02: Sai mật khẩu"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Epic sadface" in error_message
    print("✅ TC_02: wrong password")


def test_empty_username(driver):
    """TC_03: Bỏ trống Username"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username is required" in error_message
    print("✅ TC_03: empty Username")


def test_empty_password(driver):
    """TC_04: Bỏ trống Password"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Password is required" in error_message
    print("✅ TC_04: empty Password")


def test_empty_username_password(driver):
    """TC_05: Bỏ trống cả Username và Password"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username is required" in error_message
    print("✅ TC_05: empty both Username and Password")


# ===============================
# 🚀 RUN TEST CASES
# ===============================
if __name__ == "__main__":
    driver = setup_driver()
    
    try:
        test_login_success(driver)
        test_login_wrong_password(driver)
        test_empty_username(driver)
        test_empty_password(driver)
        test_empty_username_password(driver)

    finally:
        driver.quit()
        print("✅ all test case was completed!")
