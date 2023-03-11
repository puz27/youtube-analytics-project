from helper.youtube_api_manual import print_info, get_info_about_chanel


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id, self.__title, self.__description_chanel, self.__url, self.__subscriberCount_chanel, \
            self.__video_count, self.__videoCount_chanel, = get_info_about_chanel(channel_id)


    @property
    def videoCount_chanel(self):
        return self.__videoCount_chanel

    @property
    def subscriberCount_chanel(self):
        return self.__subscriberCount_chanel

    @property
    def url(self):
        return self.__url

    @property
    def description_chanel(self):
        return self.__description_chanel

    @property
    def video_count(self):
        return self.__video_count

    @property
    def title(self):
        return self.__title

    @property
    def channel_id(self):
        return self.__channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print_info(self.channel_id)


