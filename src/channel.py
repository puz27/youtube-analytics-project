from helper.youtube_api_manual import print_info, get_info_about_chanel, build, api_key
import json
import os

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

    @staticmethod
    def get_service():
        """возвращаюем объект для работы с YouTube API """
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, name_json_file):
        """Сохраняем в файл значения атрибутов экземпляра Channel"""
        parameters_of_instance = {}
        parameters_of_instance["id"] = self.__channel_id
        parameters_of_instance["title"] = self.__title
        parameters_of_instance["description_chanel"] = self.__description_chanel
        parameters_of_instance["url"] = self.__url
        parameters_of_instance["subscriberCount_chanel"] = self.__subscriberCount_chanel
        parameters_of_instance["video_count"] = self.__video_count
        parameters_of_instance["videoCount_chanel"] = self.__video_count

        json_object = json.dumps(parameters_of_instance, indent=4, ensure_ascii=False)
        path_file_statistic = os.path.join(os.getcwd(), "../statistic/" + name_json_file)

        with open(path_file_statistic, "w") as outfile:
            outfile.write(json_object)