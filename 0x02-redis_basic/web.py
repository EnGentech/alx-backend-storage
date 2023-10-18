#!/usr/bin/env python3
"""A redis approach on a website"""


import requests
from functools import wraps
from redis import Redis

r = Redis()


def track_url_count(func):
    """A decorator to track url"""

    @wraps(func)
    def wrapper(url):
        r.incr(f"count:{url}")
        return func(url)
    return wrapper


@track_url_count
def get_page(url: str) -> str:
    """A function to graps url html content"""
    response = requests.get(url)
    html_content = response.text
    r.setex(url, 10, html_content)
    return html_content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/"
    url2 = "10000/url/http://www.google.co.uk"
    test_url = url + url2
    html = get_page(test_url)
    print(html)
