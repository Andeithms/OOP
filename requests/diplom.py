import requests
from pprint import pprint
import time
from tqdm import tqdm


class User:
    url = 'https://api.vk.com/method/'

    def __init__(self, user_id, token, version):
        self.user_id = user_id
        self.token = token
        self.version = version
        self.params = {
            "user_ids": self.user_id,
            'access_token': self.token,
            'v': self.version,
            'album_id': 'profile',
            'extended': 1,
             }
        self.photos = requests.get(self.url + "photos.get", self.params).json()
        # pprint(self.photos)


    def get_photo(self):
        photo_list = []
        for i in self.photos["response"]["items"]:  # создаем список всех фото пользователя
            photo = {}
            photo['file_name'] = i['likes']['count']
            photo['size'] = i['sizes'][-1]['type']  # -1 это последнее фото с максимальным разрешением
            photo_list.append(photo)
        return photo_list

    def photo_for_upload(self):
        photo_list = []
        for i in self.photos["response"]["items"]:
            photo = {}
            photo['file_name'] = i['likes']['count']
            photo['url'] = i['sizes'][-1]['url']
            photo_list.append(photo)
        return photo_list


class YaUploader:
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN

    def upload(self, user):
        HEADERS = {'Accept': 'application/json', 'Authorization': self.TOKEN}
        photo_list = user.photo_for_upload()
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': "/photos"},
            headers=HEADERS,
        )
        response.raise_for_status()
        for photo in tqdm(photo_list):
            resp = requests.post(
                'https://cloud-api.yandex.net/v1/disk/resources/upload',
                params={'path': "/photos/" + str(photo['file_name']),
                        'url': photo['url'],
                        'overwrite': 'true'},
                headers=HEADERS,
            )
            time.sleep(1)
            resp.raise_for_status()


if __name__ == '__main__':
    uploader = YaUploader("OAuth тут был токен")
    token_vk = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
    version = '5.126'
    user_id_1 = 1234
    user_1 = User(user_id_1, token_vk, version)
    result = uploader.upload(user_1)
    pprint(user_1.get_photo())