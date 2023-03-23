from src.utils import get_playlist_info, get_duration_all_videos
import datetime


class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url, self.title = get_playlist_info(playlist_id)
        self.__total_duration = get_duration_all_videos(playlist_id)

    @property
    def total_duration(self):
        return self.__total_duration

    def show_best_video(self):
        pass

    def __str__(self):
        return f"{self.__total_duration}"
