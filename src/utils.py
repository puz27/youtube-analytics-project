from helper.youtube_api_manual import youtube, printj


def print_info(channel_id: str) -> print():
    """возвращаем информацию о канале"""
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    return printj(channel)


def get_chanel(channel_id: str) -> dict:
    """возвращаем информацию о канале в виде словаря"""
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    return channel["items"][0]


def get_info_about_chanel(channel_id: str) -> tuple:
    """получаем 7 нужных нам данных о канале"""
    formated_dictionary = get_chanel(channel_id)
    id_chanel = formated_dictionary["id"]
    title_chanel = formated_dictionary["snippet"]["title"]
    description_chanel = formated_dictionary["snippet"]["description"]
    url_chanel = "https://www.youtube.com/channel/" + channel_id
    subscriberCount_chanel = formated_dictionary["statistics"]["subscriberCount"]
    videoCount_chanel = formated_dictionary["statistics"]["videoCount"]
    viewCount_chanel = formated_dictionary["statistics"]["viewCount"]

    return id_chanel, title_chanel, description_chanel, url_chanel, subscriberCount_chanel,\
        videoCount_chanel, viewCount_chanel


def get_video_statistic(video_id: str) -> tuple:
    """возвращаем информацию о видео. название, колличество, url, колличество лайков и коментариев"""
    video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=video_id
                                           ).execute()

    video_title = video_response['items'][0]['snippet']['title']
    view_count = video_response['items'][0]['statistics']['viewCount']
    video_url = "https://youtu.be/" + video_id
    like_count = video_response['items'][0]['statistics']['likeCount']
    comment_count = video_response['items'][0]['statistics']['commentCount']

    return video_title, view_count, video_url, like_count, comment_count


def get_video_statistic_by_playlist_id(video_id: str, playlist_id: str) -> tuple or None:
    """возвращаем информацию о видео. название, колличество, url,
    колличество лайков и коментариев используя id плэйлиста и видео
    """
    playlist_response = youtube.playlistItems().list(playlistId=playlist_id,
                                                     part='contentDetails',
                                                     maxResults=50,
                                                     ).execute()

    video_ids = [video['contentDetails']['videoId'] for video in playlist_response['items']]
    if video_id in video_ids:
        return get_video_statistic(video_id)
    return None


def get_playlist_info(playlist_id: str) -> tuple:
    """По ID плэйлиста получаем описание плэйлиста и ссылку"""
    playlist_url = "https://www.youtube.com/playlist?list=" + playlist_id
    playlist_title = ""
    # достать id канала из плэйлиста
    chanel_id_response = youtube.playlistItems().list(playlistId=playlist_id,
                                                      part='snippet',
                                                      maxResults=50
                                                      ).execute()

    channel_id = chanel_id_response["items"][0]["snippet"]["channelId"]

    # по id канала можно узнать описание нужного плэйлиста
    playlist_title_response = youtube.playlists().list(channelId=channel_id,
                                                       part='contentDetails,snippet',
                                                       maxResults=50,
                                                       ).execute()

    for playlist in playlist_title_response['items']:
        if playlist["id"] == playlist_id:
            playlist_title = playlist["snippet"]["title"]
            break
        else:
            playlist_title = None
    return playlist_url,  playlist_title

# playlist_id = "PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"
# print(get_playlist_info(playlist_id))