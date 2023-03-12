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
    url_chanel = "https://www.youtube.com/channel/" + "UCMCgOm8GZkHp8zJ6l7_hIuA"
    subscriberCount_chanel = formated_dictionary["statistics"]["subscriberCount"]
    videoCount_chanel = formated_dictionary["statistics"]["videoCount"]
    viewCount_chanel = formated_dictionary["statistics"]["viewCount"]
    return id_chanel, title_chanel, description_chanel, url_chanel, subscriberCount_chanel,\
        videoCount_chanel, viewCount_chanel