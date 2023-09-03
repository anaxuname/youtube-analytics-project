import os

from googleapiclient.discovery import build


class YoutubeAPI:
    @classmethod
    def get_service(cls):
        """
        Класс-метод, возвращает объект для работы с YouTube API
        """
        api_key = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)