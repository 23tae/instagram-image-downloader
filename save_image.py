from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from time import sleep

# Replace usernames with your desired list
usernames = ["gardenpazy", "gardenplanning"]

# Set the maximum number of images to download per user
max_images_per_user = 2

# Initialize Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Define download function using requests library


def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded image: {filename}")
    else:
        print(f"Error downloading image: {image_url}")


# Loop through each username
for username in usernames:
    # Get user profile URL
    profile_url = f"https://www.instagram.com/{username}/"

    # Open the user profile
    driver.get(profile_url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "img[alt='Profile picture']"))
    )

    # Initialize downloaded image count
    downloaded_images = 0

    # Scroll through the posts
    while downloaded_images < max_images_per_user:
        # Get all post links
        post_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/p/']")

        for link in post_links:
            # Get the post URL
            post_url = link.get_attribute("href")

            # Open the post
            driver.get(post_url)

            # Wait for the image to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "img[src*='https://scontent.cdninstagram.com/']"))
            )

            # Get the image URL (assuming first image)
            image_url = driver.find_element(
                By.CSS_SELECTOR, "img[src*='https://scontent.cdninstagram.com/']").get_attribute("src")

            # Generate a unique filename
            filename = f"{username}_{downloaded_images}.jpg"

            # Download and save the image
            download_image(image_url, filename)

            downloaded_images += 1

            # Break the loop if reached the maximum download limit
            if downloaded_images >= max_images_per_user:
                break

        # Scroll down to load more posts
        sleep(2)
        driver.execute_script("window.scrollBy(0, 500)")

    # Print message
    print(f"Downloaded {downloaded_images} images for user {username}")

# Close the browser
driver.quit()
