from conf import VK_TOKEN, VK_USER_ID, VK_VERSON, VK_API_URL
import requests


class VkPhotosGet:
    def __init__(self, token=VK_TOKEN, version=VK_VERSON, photo_count=5, user_id=VK_USER_ID):
        self.token = token
        self.version = version
        self.photo_count = photo_count
        self.user_id = user_id
        self.links_list = []
        self.count_photo_likes = 0

    def get_photos(self):
        link = VK_API_URL + "photos.get"
        res = requests.get(
            link,
            params={
                "access_token": self.token,
                "v": self.version,
                "album_id": "profile",
                "count": self.photo_count,
                "extended": 1,
                "owner_id": self.user_id,
                "photo_sizes": 1,
            },
        )
        res_json = res.json()["response"]["items"]
        vk_photo_sizes = 'smxopqryzw'
        for photo in res_json:
            self.count_photo_likes = photo["likes"]["count"]
            biggest_size = max(photo["sizes"], key=lambda s: vk_photo_sizes.index(s["type"]))
            new_dict = {
                "photoID": photo["id"],
                "photo_size": biggest_size,
                "photo_type": biggest_size["type"],
            }
            self.links_list.append(new_dict)
        return self.links_list
