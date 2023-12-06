from dotenv import load_dotenv
import os
from instagrapi import Client


def main():
    # Load env file
    load_dotenv()
    ACCOUNT_USERNAME = os.getenv('ACCOUNT_USERNAME')
    ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')
    print('name: ', ACCOUNT_USERNAME)

    # Login to Instagram
    cl = Client()
    try:
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    except Exception as e:
        print('Error 1: ', e)
        return

    # Get posts
    try:
        user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
        print(user_id)
    except Exception as e:
        print('Error 2: ', e)
        return
    # medias = cl.user_medias(user_id, 5)


if __name__ == "__main__":
    main()
