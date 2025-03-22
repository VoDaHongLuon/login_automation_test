from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo Firefox WebDriver
driver = webdriver.Firefox()

# Mở trang web
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Test Case: Đăng nhập thành công
def test_login_success():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    # Kiểm tra kết quả mong đợi
    assert "inventory.html" in driver.current_url
    print("✅ Test Case: Đăng nhập thành công")

# Chạy test case
test_login_success()

# Đóng trình duyệt
driver.quit()
