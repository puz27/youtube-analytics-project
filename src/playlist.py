from src.utils import get_playlist_info


class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url, self.title = get_playlist_info(playlist_id)