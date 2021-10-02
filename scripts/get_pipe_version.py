from bs4 import BeautifulSoup
import re
import requests

from cmp_version import VersionString


def parse_page(content_soup):
    version_regex = re.compile(r'\(NMRPipe Version ([0-9\.]+) Rev ([0-9\.]+).*\)')

    versions = set()
    for i in content_soup.body():
        match = version_regex.search(str(i))
        if match:
            versions.add(f'{match.group(1)}+rev{match.group(2)}')

    if not versions:
        print('WARNING: nop version string found setting version to 0.0.0')
        versions.append('0.0.0')
    elif versions and len(versions) > 1:
        print(f'WARNING: more than one version string found ({", ".join(versions)}), taking highest!')

    versions = [VersionString(version) for version in versions]
    versions.sort()

    result = versions[-1]

    return result


def get_page():
    url = 'https://www.ibbr.umd.edu/nmrpipe/install.html'
    page = requests.get(url)

    if page.status_code != 200:
        raise Exception("couldn't load nmrpipe web page")

    return page


if __name__ == '__main__':
    page = get_page()
    soup = BeautifulSoup(page.text, 'html.parser')
    version = parse_page(soup)
    print(version)