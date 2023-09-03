import datetime

import isodate

from src.youtube import YoutubeAPI


class PlayList(YoutubeAPI):
    """Класс для PlayList"""

    def __init__(self, playlist_id):
        youtube = self.get_service()
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        self._video_response = youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()
        playlist = youtube.playlists().list(id=playlist_id, part='contentDetails,snippet').execute()
        self.title = playlist['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/playlist?list={playlist_id}'

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        """Возвращает объект класса datetime.timedelta с суммарной длительностью плейлиста"""
        for video in self._video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        most_liked_video_url = ''
        max_likes = 0
        for video in self._video_response['items']:
            if int(video['statistics']['likeCount']) > max_likes:
                max_likes = int(video['statistics']['likeCount'])
                most_liked_video_url = f'https://youtu.be/{video["id"]}'
        return most_liked_video_url
