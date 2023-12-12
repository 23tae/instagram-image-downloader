from dotenv import load_dotenv
import os


def get_account() -> dict:
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    return ({'username': username, 'password': password})
