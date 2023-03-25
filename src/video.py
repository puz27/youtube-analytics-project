from src.utils import get_video_statistic, get_video_statistic_by_playlist_id


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_title, self.view_count, self.video_url, self.like_count,\
        self.comment_count = get_video_statistic(video_id)

    def __str__(self) -> str:
        return f"{self.video_title}"


class PLVideo():
    def __init__(self, video_id, playlist_id) -> None:
        self.video_title, self.view_count, self.video_url, self.like_count, \
        self.comment_count = get_video_statistic_by_playlist_id(video_id, playlist_id)

    def __str__(self) -> str:
        return f"{self.video_title}"
