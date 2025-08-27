from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 자동화 제어 메시지 숨기기 옵션
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--user-data-dir=C:/emp/selenium") 

# ChromeDriver 드라이버 경로
chrome_driver_path = "C:/python/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 로그인 페이지 접속
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

# 로그인 정보 입력
driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# 로그인 성공 메시지 기다리기
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

# 로그인 성공 여부 확인
success_message = driver.find_element(By.ID, "flash").text
if "You logged into a secure area!" in success_message:
    print("Login Test Passed")
    driver.execute_script("alert('로그인 성공!')")
    time.sleep(2)
    driver.switch_to.alert.accept()
else:
    print("Login Test Failed")

# 로그아웃 버튼 기다리기
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.button.secondary.radius'))
)
time.sleep(2)

# 로그아웃 클릭
driver.find_element(By.CSS_SELECTOR, 'a.button.secondary.radius').click()
time.sleep(5)

# 로그아웃 메시지 확인
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "flash"))
)
time.sleep(5)

# 로그아웃 성공 확인
if "You logged out of the secure area!" in driver.page_source:
    print("Logout Test Passed")
else:
    print("Logout Test Failed")

# 종료
driver.quit()