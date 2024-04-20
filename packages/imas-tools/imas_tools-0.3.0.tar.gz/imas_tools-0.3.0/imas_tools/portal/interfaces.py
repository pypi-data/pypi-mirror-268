from typing import List, Optional, Any, Literal, get_args, Type
from typing_extensions import TypedDict

BRAND_CODE = Literal[
    "IDOLMASTER", "CINDERELLAGIRLS", "MILLIONLIVE", "SIDEM", "SHINYCOLORS", "GAKUEN", "OTHER"
]

SUBCATEGORY_CODE = Literal[
    "GAME",
    "EVENT",
    "ANIME",
    "LIVESTREAM",
    "RADIO",
    "GOODS",
    "OTHER",
    "DVD-BD",
    "BOOK",
    "CD",
    "COLLABO-CAMP",
]

class InvalidBrandCode(ValueError):
    pass


class InvalidSubcategoryCode(ValueError):
    pass


def validate_brand_code(value: str):
    if is_literal_str(value, BRAND_CODE):
        return
    raise InvalidBrandCode(f"Invalid brand code: {value}")

def validate_subcategory_code(value: str):
    if is_literal_str(value, SUBCATEGORY_CODE):
        return
    raise InvalidSubcategoryCode(f"Invalid subcategory code: {value}")

def is_literal_str(value: str, typ) -> bool:
    return isinstance(value, str) and value in get_args(typ)


class Brand(TypedDict):
    name: str
    code: BRAND_CODE


class Subcategory(TypedDict):
    name: str
    code: SUBCATEGORY_CODE


class Categories(TypedDict):
    name: str
    subcategory: List[Subcategory]
    code: str


class RepeatPattern(TypedDict, total=False):
    date: int
    repeat_startdate: int
    kind: str
    days: List[int]
    repeat_pattern: List[Any]
    repeat_enddate: int
    exceptions: List[int]


class ArticleList(TypedDict, total=False):
    content: str
    information: str
    event_enddate: int
    event_url: str
    startdate: int
    branch_no: int
    _p_key: str
    site: str
    _id: str
    region: str
    path: str
    display_state_during_period: str
    dspdate: Any
    ip: str
    brand: List[Brand]
    event_startdate: int
    listed_subcategories: str
    repeat: bool
    repeat_pattern: RepeatPattern
    updated: int
    enddate: int
    publish_status: str
    categories: Categories
    delflg: str
    event_dspdate: str
    title: str
    event_place: Any
    news_thumbnail: Any
    hashtag: Any
    thumbnail: str
    filename: str
    sp_thumbnail: str
    url: str


class CalendarResponse(TypedDict):
    apiStatus: bool
    total_count: int
    start: int
    limit: int
    count: int
    time: int
    article_list: List[ArticleList]
