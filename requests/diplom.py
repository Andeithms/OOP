import requests
from pprint import pprint
import time
from tqdm import tqdm
import json


class User:
    url = 'https://api.vk.com/method/'

    def __init__(self, user_id, token, version):
        self.owner_id = user_id
        self.token = token
        self.version = version
        self.params = {
            'owner_id': self.owner_id,
            'access_token': self.token,
            'v': self.version,
            'album_id': 'profile',
            'extended': 1,
             }
        self.photos = requests.get(self.url + "photos.get", self.params).json()
        pprint(self.photos)


    def creating_json(self):
        photo_list = []
        for i in self.photos["response"]["items"]:  # создаем список всех фото пользователя
            photo = {}
            count_like = i['likes']['count']
            photo['file_name'] = count_like
            for x in photo_list:    # проверка фото на одинаковое кол-во лайков
                if x['file_name'] == count_like:
                    photo['file_name'] = str(count_like) + '.' + str(i['date'])    # . - разделитель лайков и даты
            photo['size'] = i['sizes'][-1]['type']  # -1 это последнее фото с максимальным разрешением
            photo_list.append(photo)
        with open('D:\projects\photo.json', 'w') as file_work:
            json.dump(photo_list, file_work)
        return photo_list


    def photo_for_upload(self):
        photo_list = []
        for i in self.photos["response"]["items"]:
            photo = {}
            count_like = i['likes']['count']
            photo['file_name'] = count_like
            for x in photo_list:
                if x['file_name'] == count_like:
                    photo['file_name'] = str(count_like) + '.' + str(i['date'])
            photo['url'] = i['sizes'][-1]['url']
            photo_list.append(photo)
        return photo_list


class YaUploader:
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN
        self.HEADERS = {'Accept': 'application/json', 'Authorization': self.TOKEN}

    def checking_my_yandex_disc(self):
        checking_folders = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                        params={'path': "/"},
                                        headers=self.HEADERS,
                                        )
        checking_folders.raise_for_status()
        data = checking_folders.json()
        return data

    def creating_folder(self):
        data = self.checking_my_yandex_disc()
        input_folder = input('Введите имя папки, в которую хотите загрузить фото ')

        for file in data['_embedded']['items']:
            if input_folder == file['name']:
                print('Такая папка уже существует, хотите загрузить в нее?')
                user_answer = input('yes/no ')
                if user_answer == 'yes':
                    break
                else:
                    return self.creating_folder()

        requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                     params={'path': "/" + str(input_folder)},
                     headers=self.HEADERS,
                     )
        return input_folder


    def upload(self, user):
        folder_name = self.creating_folder()
        photo_list = user.photo_for_upload()
        for photo in tqdm(photo_list):
            requests.post(
                'https://cloud-api.yandex.net/v1/disk/resources/upload',
                params={'path': "/" + folder_name + "/" + str(photo['file_name']),
                        'url': photo['url'],
                        'overwrite': 'true'},
                headers=self.HEADERS,
            )

            time.sleep(1)
        return 'Фото загружены'


if __name__ == '__main__':
    # user_input_vk = input('Введите токен vk ')
    user_input_id = input('Введите id vk(например: 133423499) ')
    token_input_ya = input('Введите токен Яндекса ')
    token_input_vk = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
    version = '5.126'
    user_1 = User(user_input_id, token_input_vk, version)
    uploader = YaUploader("OAuth " + token_input_ya)
    print(uploader.upload(user_1))
    user_1.creating_json()