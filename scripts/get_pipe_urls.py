from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

from cmp_version import VersionString


def parse_page(content_soup):
    anchors = content_soup.find_all('a')
    parts = [[elem.get('href'), elem.parent.parent] for elem in anchors]
    return parts


def select_urls(urls):
    result = []
    for url in urls:
        base_url = url[0]
        extension = base_url.split('.')[-1]
        if extension in ['tZ', 'com']:
            result.append(url)
    return result


def get_page():
    PIPE_URL = 'https://www.ibbr.umd.edu/nmrpipe/install.html'
    pipe_page = requests.get(PIPE_URL)

    if pipe_page.status_code != 200:
        raise Exception("couldn't load nmrpipe web page")

    return pipe_page


if __name__ == '__main__':
    page = get_page()
    soup = BeautifulSoup(page.text, 'html.parser')
    found_urls = parse_page(soup)
    found_urls = select_urls(found_urls)

    result = [['url', 'bytes', 'cksum']]
    for found_url in found_urls:

        row = found_url[1]
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        elements = [ele for ele in cols if ele]

        if elements and isinstance(elements, list):
            if elements[0].startswith('File'):
                if len(elements) > 5:
                    bytes = elements[4].replace(',','').replace('bytes', '')
                    chksum = elements[5]
                else:
                    bytes  = '.'
                    chksum = '.'
                result.append([found_url[0],bytes, chksum])
    print(tabulate(result, tablefmt='plain'))