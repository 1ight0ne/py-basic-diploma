import os
import json
import logging
import requests
from datetime import datetime

from alive_progress import alive_bar

from conf import YA_TOKEN
from vk_photos_get import VkPhotosGet


class YandexUpload(VkPhotosGet):
    def upload(self, photos_folder, token=YA_TOKEN):
        YA_API = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            "Accept": "application/json",
            "Authorization": f"OAuth {token}"
        }
        return_list = []
        logging.info("Копирование на Yandex.Disk")
        with alive_bar(len(self.photos_list)) as bar:
            for el in self.photos_list:
                bar()
                file_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f'{el["likes"]}_{file_datetime}.jpeg'
                result = requests.post(
                    YA_API,
                    headers=headers,
                    params={
                        "url": el["photo_size"]["url"],
                        "disable_redirects": False,
                        "path": f'/{photos_folder}/{file_name}'
                    }
                )
                if result.status_code != 202:
                    logging.error(f"ошибка! Код: {result.status_code} {result.json()}")
                    return result
                return_dict = {
                    "file_name": file_name,
                    "size": el["photo_type"]
                }
                return_list.append(return_dict)
        logging.info('Загрузка завершена')
        return return_list


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    new_upload = YandexUpload()
    new_upload.get_photos()
    output_file = os.path.join(os.path.dirname(__file__), 'output.json')
    with open(output_file, "w") as f:
        json.dump(new_upload.upload('netology_test'),
                  f, ensure_ascii=False, indent=2)
