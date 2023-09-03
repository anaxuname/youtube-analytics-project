import os
from googleapiclient.discovery import build


class Video:
    """Класс для Video"""
    def __init__(self, video_id: str):
        """Экземпляр инициализируется через id канала. Данные подтягиваются по API."""
        self.video_id = video_id
        youtube = self.get_service()
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
        self.url: str = f'https://youtu.be/{video_id}'

    @classmethod
    def get_service(cls):
        """
        Класс-метод, возвращает объект для работы с YouTube API
        """
        api_key = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def __str__(self):
        """
        Метод, возвращает название и ссылку на канал по шаблону <название_канала> (<ссылка_на_канал>)
        """
        return self.video_title


class PLVideo(Video):
    """Класс наследуется от Video, поэтому используем метод super()"""
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id: str = playlist_id