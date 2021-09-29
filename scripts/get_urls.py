import sys
from urllib.parse import urlparse
import os

if __name__ == '__main__':
    with open(sys.argv[1]) as fh:
        next(fh)
        for line in fh:
            url = line.split()[0]
            file_name = os.path.basename(urlparse(url).path)
            print(url, file_name)
