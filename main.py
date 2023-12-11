import read_file
import user_info
import download_images

file_path = './data/users.txt'


def main():
    my_account = user_info.get_account()
    profiles = read_file.get_profiles(file_path)
    download_images.run_webdriver(my_account, profiles)


if __name__ == '__main__':
    main()
