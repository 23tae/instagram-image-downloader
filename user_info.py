from dotenv import load_dotenv
import os


def get_account() -> tuple:
    load_dotenv()
    username = os.getenv('ACCOUNT_USERNAME')
    password = os.getenv('ACCOUNT_PASSWORD')
    return (username, password)
