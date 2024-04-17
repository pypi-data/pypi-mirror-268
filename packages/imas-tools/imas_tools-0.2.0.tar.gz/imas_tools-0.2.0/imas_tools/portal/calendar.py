from typing_extensions import Never
import requests, json, time, pytz
from calendar import monthrange
from datetime import datetime, timedelta
from .interfaces import BRAND_CODE, SUBCATEGORY_CODE, CalendarResponse

def fetch_news_for_today():
    return NotImplemented


def fetch_articles_for_today(
    brands: list[BRAND_CODE] = [],
    subcategories: list[SUBCATEGORY_CODE] = [],
):
    japan_timezone = pytz.timezone("Asia/Tokyo")
    now_in_japan = datetime.now(japan_timezone)

    midnight_today = japan_timezone.localize(
        datetime(now_in_japan.year, now_in_japan.month, now_in_japan.day, 0, 0, 0)
    )
    midnight_tomorrow = midnight_today + timedelta(days=1)
    return _fetch_articles(
        midnight_today,
        midnight_tomorrow,
        brands,
        subcategories,
    )


def fetch_articles_for_month(
    year: int = 0,
    month: int = 0,
    brands: list[BRAND_CODE] = [],
    subcategories: list[SUBCATEGORY_CODE] = [],
):
    # 设置日本时区
    japan_timezone = pytz.timezone("Asia/Tokyo")

    if year == 0:
        year = datetime.now(japan_timezone).year

    if month == 0:
        month = datetime.now(japan_timezone).month

    # 计算本月第一天和最后一天
    first_day_this_month = japan_timezone.localize(
        datetime(year, month, 1, 0, 0, 0)
    )
    last_day = monthrange(year, month)[1]
    last_day_this_month = japan_timezone.localize(
        datetime(year, month, last_day, 0, 0, 0)
    )

    # 计算下月的第一天（即本月最后一天的24点）
    first_day_next_month = last_day_this_month + timedelta(days=1)

    return _fetch_articles(
        first_day_this_month,
        first_day_next_month,
        brands,
        subcategories,
    )


# Not Recommended to use because arbitary api call may not occur from idolmaster portal
# This interface is for internal use
def _fetch_articles(
    start_date: datetime,
    end_date: datetime,
    brands: list[BRAND_CODE] = [],
    subcategories: list[SUBCATEGORY_CODE] = [],
    limit=200,
) -> CalendarResponse:
    base_url = "https://cmsapi-frontend.idolmaster-official.jp/sitern/api/idolmaster/Article/list"

    target_start_date = start_date.astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    target_end_date = end_date.astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    params = {
        "site": "jp",
        "ip": "idolmaster",
        "token": _get_token(),
        "sort": "asc",
        "limit": limit,
        "data": {
            "category": ["SCHEDULE"],
            "brand": brands,
            "subcategory": subcategories,
            "target_start_date": target_start_date,
            "target_end_date": target_end_date,
        },
    }

    params["data"] = json.dumps(params["data"])

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ja",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()["data"]
    else:
        response.raise_for_status()
        return Never


def _get_token() -> str:
    time.sleep(0.1)
    # Define the URL
    url = "https://cmsapi-frontend.idolmaster-official.jp/sitern/api/cmsbase/Token/get"

    # Set up the headers as given in the fetch request
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ja",
        "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    # Additional options from fetch request translated to requests library
    cookies = {
        # Cookies must be set if needed, fetch has "credentials": "include"
    }
    # In requests, referrer and referrerPolicy do not have direct equivalents,
    # but can be added to headers if necessary.

    # Send the GET request
    response = requests.get(url, headers=headers, cookies=cookies)

    # Print the response text (or process it in other ways)
    return response.json()["data"]["token"]
