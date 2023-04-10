import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_filename(self, path_to_file: str):
        abs_path = os.path.abspath(path_to_file)
        name = os.path.basename(fr'{abs_path}')
        return name

    def _get_upload_link(self, path_to_file_yadisk):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file_yadisk, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file_yadisk: str, file_for_upload: str):
        href = self._get_upload_link(path_to_file_yadisk=path_to_file_yadisk).get("href")
        response = requests.put(href, data=open(file_for_upload, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    URL = "https://cloud-api.yandex.net/v1/disk/resources"
    file_for_upload = 'test.txt'
    token = ""
    uploader = YaUploader(token)
    path_to_file_yadisk = uploader.get_filename(file_for_upload)
    result = uploader.upload(path_to_file_yadisk, file_for_upload)
