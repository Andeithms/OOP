import requests


class User:
    url = 'https://api.vk.com/method/'
    same_friend_list = []

    def __init__(self, user_id, token, version):
        self.user_id = user_id
        self.token = token
        self.version = version
        self.params = {
            "user_ids": self.user_id,
            'access_token': self.token,
            'v': self.version,
            "fields": "domain"
             }
        self.basic_fields = requests.get(self.url + "users.get", self.params).json()
        self.friends = requests.get(self.url + "friends.get", {
             "user_id": self.user_id,
             "access_token": self.token,
             "v": self.version
        }).json()


    def __and__(self, otheruser):
      for i in self.friends["response"]["items"]:
          if i in otheruser.friends["response"]["items"]:
              self.same_friend_list.append(User(i, self.token, self.version))
      return self.same_friend_list


    def __str__(self):
        return "https://vk.com/id" + str(self.basic_fields["response"][0]["id"])


token = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
version = '5.126'
user_id_1 = 3383465
user_id_2 = 77215497
user_1 = User(user_id_1, token, version)
user_2 = User(user_id_2, token, version)
same_friend_list = user_1 & user_2
print(same_friend_list)
print(user_1)
