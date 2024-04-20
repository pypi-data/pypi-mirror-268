import requests, json, re
from typing import Dict, Any, TypedDict, Union
from urllib.parse import quote
from bs4 import BeautifulSoup

class LyricMetadata(TypedDict):
    title: str
    artist: str
    composer: str
    lyricist: str
    lyrics: str

def is_valid_json(json_str):
    try:
        # 使用json.loads尝试解析字符串
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        # 如果解析失败，返回False
        return False


def find_json_object_in_string(s: str):

    start_c = "{"
    end_c = "}"

    start = s.find(start_c)
    end = s.rfind(end_c)

    if end == -1 or start >= end:
        raise Exception("No matching closing bracket found")

    if is_valid_json(s[start : end + 1]):
        return s[start : end + 1]

    return find_json_object_in_string(s[start:end])


def query_song(song_name: str) -> Dict[str, Any]:  # type: ignore
    res = requests.get(
        f"https://recochoku.jp/search/song?q={quote(song_name)}&type=SINGLE",
    )
    soup = BeautifulSoup(res.content, "html.parser")
    scripts = soup.find_all("script")

    keyword = "var musicList ="

    # 遍历所有 script 标签并打印其中的文本内容：
    for script in scripts:
        if keyword in script.get_text():
            for line in script.get_text().split("\n"):
                if keyword in line:
                    return json.loads(find_json_object_in_string(line))


def query_track_id(music_id) -> int:
    res = requests.get(
        f"https://recochoku.jp/song/S{music_id}",
    )
    soup = BeautifulSoup(res.content, "html.parser")
    scripts = soup.find_all("script")
    keyword = "trackId = "
    for script in scripts:
        if keyword in script.get_text():
            for line in reversed(script.get_text().split("\n")):
                if keyword in line:
                    pattern = r"\d+"

                    matches = re.findall(pattern, line)
                    return int(matches[0])
    raise Exception("Track ID not found")


def query_metadata_from_api_store(track_id):
    res = requests.get(
        f"https://common-api-store.recochoku.jp/lyrics/{track_id}",
        headers={
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5",
            "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "x-sec-ch-ua-platform-version": "15.0.0",
            "Referer": "https://recochoku.jp/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        },
    )
    tmp = res.json()
    composer = tmp.get("composer")
    lyricist = tmp.get("lyricist")
    artist = tmp.get("artist")
    lyrics = get_lyrics_from_words(tmp.get("words"))
    return {
        "composer": composer,
        "lyricist": lyricist,
        "artist": artist,
        "lyrics": lyrics,
    }


def get_lyrics_from_words(words: Union[str, None]):
    if words is None:
        return ""
    rtn = ""
    for word in json.loads(words):
        rtn += chr(word)
    return rtn


def query_metadata_for(music_name: str, choice: int = 0) -> LyricMetadata:
    rtn = query_song(music_name)
    if choice > len(rtn["music"]):
        raise Exception(f"Choice index out of range: only {choice} choices are returned")
    music_id = rtn["music"][choice]["musicId"]
    track_name = rtn["music"][choice]["title"]
    artist_name = rtn["music"][choice]["artist"]["name"]
    track_id = query_track_id(music_id)
    metadata = query_metadata_from_api_store(track_id)
    return {
        "title": track_name,
        "artist": artist_name,
        "composer": metadata["composer"],
        "lyricist": metadata["lyricist"],
        "lyrics": metadata["lyrics"],
    }
