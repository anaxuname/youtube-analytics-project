import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        youtube = self.get_service()
        self.__channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.__channel_id = channel_id
        self.__title = self.__channel["items"][0]["snippet"]["title"]
        self.__description = self.__channel["items"][0]["snippet"]["description"]
        self.__video_count = self.__channel["items"][0]["statistics"]["videoCount"]
        self.__view_count = self.__channel["items"][0]["statistics"]["viewCount"]
        self.__subscriber_count = self.__channel["items"][0]["statistics"]["subscriberCount"]
        self.__url = f"https://www.youtube.com/channel/{channel_id}"


    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def video_count(self):
        return self.__video_count

    @property
    def view_count(self):
        return self.__view_count

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def url(self):
        return self.__url

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """
        Сохраняет в файл значения атрибутов экземпляра Channel
        """
        with open(file_name, 'w') as outfile:
            json.dump(self.__channel, outfile)

    @classmethod
    def get_service(cls):
        """
        Класс-метод, возвращает объект для работы с YouTube API
        """
        api_key = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)
