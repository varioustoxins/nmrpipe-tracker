import os
import sys
from urllib.parse import urlparse

def url_to_filename(url):
    return os.path.basename(urlparse(url).path)

if __name__ == '__main__':
    print(url_to_filename(sys.argv[1]))