import requests
import os


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_upload(self, disk_file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Autorization': f'OAuth {self.token}',
            'Content - Type': 'application/json'
        }
        params = {'path': disk_file_path, 'overwrate': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, disk_file_path, file_name):
        response_href = self.get_upload(disc_file_path=disk_file_path)
        href = response_href.get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.statys_code == 201:
            print('Загружено успешно')

    if __name__ == '__main__':
        ya = YaUploader(token = 'token')
        ya.upload_file(disk_file_path = 'нетология/ДЗ29', file_name = 'home_work.txt')
