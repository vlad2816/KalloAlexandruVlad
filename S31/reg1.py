import requests
import time

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
URL = "https://jsonplaceholder.typicode.com/comments"


def get_with_retry(url):
    try:
        response = requests.get(POSTS_URL, timeout=(3.5, 30))
    except requests.ReadTimeout:
        print("conecction timed out. Retry in 3 sec")
        time.sleep(3)
        get_with_retry(url)
    else:
        response.raise_for_status()
        return response.json()


try:
    print(get_with_retry(POSTS_URL))
except requests.RequestException as err:
    print(err)
