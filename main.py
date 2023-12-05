from dotenv import load_dotenv
import os 
from instagrapi import Client

# Load env file
load_dotenv()
ACCOUNT_USERNAME = os.getenv('ACCOUNT_USERNAME')
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')

# Login to Instagram
cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# Get posts
user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
medias = cl.user_medias(user_id, 5)