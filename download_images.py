from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import ssl
import os

image_number = 20


def run_webdriver(my_account: dict, profiles: list[tuple]):
    driver = set_options()
    move_main_page(my_account, driver)
    for profile in profiles:
        category, name = profile
        save_image(driver, category, name)
    driver.quit()


def set_options():
    ssl._create_default_https_context = ssl._create_unverified_context
    # 브라우저 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    chrome_options.add_argument('incognito')
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def move_main_page(my_account: dict, driver: webdriver):
    # 페이지 이동
    driver.get("https://instagram.com")
    # 인스타그램 로그인
    driver.implicitly_wait(10)
    login_id = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    login_id.send_keys(my_account['username'])
    login_pwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    login_pwd.send_keys(my_account['password'])
    driver.implicitly_wait(10)
    login_id.send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, '._ac8f').click()  # 로그인 정보 저장 안함
    time.sleep(2)


def save_image(driver, category, name):
    print('Downloading images of ' + name)
    profile_url = 'https://www.instagram.com/' + name
    driver.get(profile_url)

    driver.implicitly_wait(15)
    # 첫 번째 사진 클릭
    driver.find_element(By.CSS_SELECTOR, '._aagw').click()

    driver.implicitly_wait(15)
    out_dir = os.path.join(os.getcwd(), 'result', category, name)
    os.path.exists(out_dir) or os.makedirs(out_dir)

    for i in range(image_number):
        try:
            img_elements = driver.find_elements(
                By.CSS_SELECTOR, '._aatk .x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
            if img_elements == None:
                driver.find_element(
                    By.CSS_SELECTOR, '._aaqg ._abl-').click()  # 다음 버튼 클릭
                continue
            img_src = img_elements[0].get_attribute('src')
            urllib.request.urlretrieve(img_src, f'{out_dir}/{i}.jpg')

            driver.find_element(
                By.CSS_SELECTOR, '._aaqg ._abl-').click()  # 다음 버튼 클릭
        except Exception as e:
            print(f"Error downloading image: {e}")
            driver.find_element(
                By.CSS_SELECTOR, '._aaqg ._abl-').click()  # 다음 버튼 클릭
