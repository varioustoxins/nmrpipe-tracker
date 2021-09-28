from bs4 import BeautifulSoup
import re
import requests

from cmp_version import VersionString


def parse_page(content_soup):

    return [elem.get('href') for elem in content_soup.find_all('a')]


def select_urls(urls):
    return [url for url in urls  if url is not None and url.split('.')[-1] in ['tZ', 'com']]


def get_page():
    PIPE_URL = 'https://www.ibbr.umd.edu/nmrpipe/install.html'
    pipe_page = requests.get(PIPE_URL)

    if pipe_page.status_code != 200:
        raise Exception("couldn't load nmrpipe web page")

    return pipe_page


if __name__ == '__main__':
    page = get_page()
    soup = BeautifulSoup(page.text, 'html.parser')
    urls = parse_page(soup)
    urls = select_urls(urls)
    urls = set(urls)
    for url in urls:
        print(url)