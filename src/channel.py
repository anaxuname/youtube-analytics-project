import json

from src.youtube import YoutubeAPI


class Channel(YoutubeAPI):
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
        self.__subscriber_count = int(self.__channel["items"][0]["statistics"]["subscriberCount"])
        self.__url = f"https://www.youtube.com/channel/{channel_id}"

    def __str__(self):
        """
        Метод, возвращает название и ссылку на канал по шаблону <название_канала> (<ссылка_на_канал>)
        """
        return f"{self.__title} ({self.__url})"

    def __add__(self, other):
        """
        Возвращение сложения двух экземпляров класса по числу подписчиков
        """
        if type(other) == Channel:
            return self.__subscriber_count + other.__subscriber_count
        else:
            raise TypeError

    def __sub__(self, other):
        """
        Возвращение вычитания двух экземпляров класса по числу подписчиков
        """
        return self.__subscriber_count - other.__subscriber_count

    def __gt__(self, other):
        """
        Возвращение сравнения "больше" двух экземпляров класса по числу подписчиков
        """
        return self.__subscriber_count > other.__subscriber_count

    def __ge__(self, other):
        """
        Возвращение сравнения "больше или равно" двух экземпляров класса по числу подписчиков
        """
        return self.__subscriber_count >= other.__subscriber_count

    def __lt__(self, other):
        """
        Возвращение сравнения "меньше" двух экземпляров класса по числу подписчиков
        """
        return self.__subscriber_count < other.__subscriber_count

    def __le__(self, other):
        """
        Возвращение сравнения "меньше или равно" двух экземпляров класса по числу подписчиков
        """
        return self.__subscriber_count <= other.__subscriber_count

    def __eq__(self, other):
        """
        Возвращение сравнения "равно" двух экземпляров класса по числу подписчиков
        """
        return self.__subscriber_count == other.__subscriber_count

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
