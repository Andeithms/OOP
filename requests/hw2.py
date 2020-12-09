import requests
import time


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {"Auhtorization": self.token}
        resp = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': '/music'},
            headers=HEADERS,
        )
        resp.raise_for_status()
        time.sleep(5)
        data = resp.json()
        url_for_load = data['href']
        resp_up = requests.put(url_for_load, data=file_path,)
        resp_up.raise_for_status()
        return 'загрузка успешна'


if __name__ == '__main__':
    uploader = YaUploader("OAuth мой токен")    # токен убран
    result = uploader.upload('D:/music/Architects - Black Lungs.mp3')