import bs4
import requests
import re
import json
import random

USER_AGENTS = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),
    ("Mozilla/5.0 (Windows NT 6.1; WOW64) "
     "AppleWebKit/537.36 (KHTML, like Gecko) "
     "Chrome/ 58.0.3029.81 Safari/537.36"),
]


def search_youtube(query, location_code="US"):
    base_url = "https://www.youtube.com"
    headers = {
        'User-Agent': random.choice(USER_AGENTS)
    }
    params = {"search_query": query,
              "gl": location_code}
    url = 'https://www.youtube.com/results'
    html = requests.get(url, headers=headers, params=params).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    blob = str(soup.find('script', string=re.compile('ytInitialData')))
    s = """window["ytInitialData"] = """
    e = """;
    window["ytInitialPlayerResponse"] = null;"""
    json_text = blob.split(s)[1].split(e)[0]
    # print(json_text)
    results = json.loads(json_text)
    data = {}

    videos = []
    playlists = []
    related_to_search = []
    related_queries = []
    radio = []

    contents = results['contents']['twoColumnSearchResultsRenderer']
    primary = contents["primaryContents"]["sectionListRenderer"][
        "contents"][0]['itemSectionRenderer']['contents']
    # secondary = contents["secondaryContents"][
    # "secondarySearchContainerRenderer"]["contents"][0]
    featured_channel = {"videos": []}

    # because order is not assured we need to make 2 passes over the data
    for idx, vid in enumerate(primary):
        if 'channelRenderer' in vid:
            vid = vid['channelRenderer']
            title = vid["title"]["simpleText"]
            # Channel info but no vids
            featured_channel["title"] = title

    for idx, vid in enumerate(primary):
        if 'videoRenderer' in vid:
            vid = vid['videoRenderer']
            thumb = vid["thumbnail"]['thumbnails']
            title = vid["title"]["runs"][0]["text"]
            length_caption = \
                vid["lengthText"]['accessibility']["accessibilityData"][
                    "label"]
            length_txt = vid["lengthText"]['simpleText']
            videoId = vid['videoId']
            url = \
                vid['navigationEndpoint']['commandMetadata'][
                    'webCommandMetadata'][
                    'url']

            videos.append(
                {
                    "url": base_url + url,
                    "title": title,
                    "length": length_txt,
                    "length_human": length_caption,
                    "videoId": videoId,
                    "thumbnails": thumb
                }
            )

        elif 'shelfRenderer' in vid:
            entries = vid['shelfRenderer']
            # most recent from channel {title_from_step_above}
            # related to your search

            category = entries["title"]["simpleText"]
            # TODO category localization
            # this comes in lang from your ip address
            # not good to use as dict keys, can assumptions be made about
            # ordering and num of results? last item always seems to be
            # related artists and first (if any) featured channel
            ch = featured_channel.get("title", "")

            for vid in entries["content"]["verticalListRenderer"]['items']:
                vid = vid['videoRenderer']
                thumb = vid["thumbnail"]['thumbnails']
                title = vid["title"]["runs"][0]["text"]
                length_caption = \
                    vid["lengthText"]['accessibility']["accessibilityData"][
                        "label"]
                length_txt = vid["lengthText"]['simpleText']
                videoId = vid['videoId']
                url = vid['navigationEndpoint']['commandMetadata'][
                    'webCommandMetadata']['url']

                if ch and category.endswith(ch):
                    featured_channel["videos"].append(
                        {
                            "url": base_url + url,
                            "title": title,
                            "length": length_txt,
                            "length_human": length_caption,
                            "videoId": videoId,
                            "thumbnails": thumb
                        }
                    )
                else:
                    related_to_search.append(
                        {
                            "url": base_url + url,
                            "title": title,
                            "length": length_txt,
                            "length_human": length_caption,
                            "videoId": videoId,
                            "thumbnails": thumb,
                            "reason": category
                        }
                    )

        elif 'playlistRenderer' in vid:
            # playlist
            vid = vid['playlistRenderer']
            playlist = {
                "title": vid["title"]["simpleText"]
            }
            vid = vid['navigationEndpoint']
            playlist["url"] = \
                base_url + vid['commandMetadata']['webCommandMetadata']['url']
            playlist["videoId"] = vid['watchEndpoint']['videoId']
            playlist["playlistId"] = vid['watchEndpoint']['playlistId']
            playlists.append(playlist)

        elif 'horizontalCardListRenderer' in vid:
            # alternative search (related artists)
            for vid in vid['horizontalCardListRenderer']['cards']:
                vid = vid['searchRefinementCardRenderer']
                url = \
                    vid['searchEndpoint']['commandMetadata'][
                        "webCommandMetadata"][
                        "url"]
                related_queries.append({
                    "title": vid['searchEndpoint']['searchEndpoint']["query"],
                    "url": base_url + url,
                    "thumbnails": vid["thumbnail"]['thumbnails']
                })

        elif 'radioRenderer' in vid:
            # playlist data
            vid = vid['radioRenderer']
            title = vid["title"]["simpleText"]
            thumb = vid["thumbnail"]['thumbnails']
            vid = vid['navigationEndpoint']
            url = vid['commandMetadata']['webCommandMetadata']['url']
            videoId = vid['watchEndpoint']['videoId']
            playlistId = vid['watchEndpoint']['playlistId']
            radio.append({
                "title": title,
                "thumbnails": thumb,
                "url": base_url + url,
                "videoId": videoId,
                "playlistId": playlistId
            })

    data["videos"] = videos
    data["playlists"] = playlists
    data["featured_channel"] = featured_channel
    data["related_videos"] = related_to_search
    data["related_queries"] = related_queries
    return data
