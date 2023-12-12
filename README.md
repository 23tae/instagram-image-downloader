# Instagram Image Downloader

## About

- Selenium을 사용한 인스타그램 이미지 크롤러

## Usage

1. `./data/users.txt`에 다음과 같은 형식으로 작성 (hashtag: 이미지가 저장될 상위 디렉토리명, user: 크롤링할 유저명)

```
<hashtag>
garden
<user>
user1
user2
<hashtag>
food
<user>
user3
user4
```

2. `python3 main.py`로 실행

- 현재 수집 개수: 20 (`download_images.py`의 `image_number` 변경)

3. 이미지는 `./result/<hashtag>/<user>/`에 저장됨
