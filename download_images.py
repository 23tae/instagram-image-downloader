from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import ssl
import user_info
import os

username, password = user_info.get_account()
print('<User info>\nusername:', username)
name = 'gardenpazy'

ssl._create_default_https_context = ssl._create_unverified_context

# 브라우저 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
chrome_options.add_argument('incognito')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options)

# 페이지 이동
driver.get("https://instagram.com")
# 인스타그램 자동로그인
driver.implicitly_wait(10)
login_id = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
login_id.send_keys(username)
login_pwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
login_pwd.send_keys(password)
driver.implicitly_wait(10)
login_id.send_keys(Keys.ENTER)

time.sleep(4)
driver.find_element(By.CSS_SELECTOR, '._ac8f').click()  # 로그인 정보 저장 안함

time.sleep(2)
profile_url = 'https://www.instagram.com/' + name
driver.get(profile_url)

driver.implicitly_wait(15)
# 첫번째 사진 클릭
first_img = driver.find_element(By.CSS_SELECTOR, '._aagw').click()

driver.implicitly_wait(15)
out_dir = os.path.join(os.getcwd(), name)
os.path.exists(out_dir) or os.makedirs(out_dir)

for i in range(10):
    try:
        img_elements = driver.find_elements(
            By.CSS_SELECTOR, '._aatk .x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
        if img_elements == None:
            # Click next button
            driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
            continue
        img_src = img_elements[0].get_attribute('src')
        urllib.request.urlretrieve(img_src, f'{out_dir}/{i}.jpg')

        # Click next button
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()
    except Exception as e:
        # Handle exceptions
        print(f"Error downloading image: {e}")
        # Click next button
        driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-').click()

driver.quit()
