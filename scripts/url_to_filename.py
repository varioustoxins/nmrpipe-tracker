import os
import sys
from urllib.parse import urlparse

if __name__ == '__main__':

    print(os.path.basename(urlparse(sys.argv[1]).path))