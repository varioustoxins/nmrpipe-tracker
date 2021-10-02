import os
import sys
from pathlib import Path
import pycksum

from url_to_filename import url_to_filename

EXIT_ERROR = 1

if __name__ == '__main__':
    with open(sys.argv[1]) as fh:

        print(next(fh).strip(), file=sys.stderr)

        for line in fh:
            line = line.strip()
            url,  bytes, chksum = line.split()
            file_name = url_to_filename(url)


            print(line, file=sys.stderr)

            path = Path('MIRROR') / file_name
            if bytes != '.':
                bytes = int(bytes)
                bytes_on_file_system = os.path.getsize(path)
                if bytes !=  bytes_on_file_system:
                    print(f'Error: size of file from url {url} does not match (expected {bytes} bytes got {bytes_on_file_system} bytes)', file=sys.stderr)
                    print('Exiting..', file=sys.stderr)
                    sys.exit(EXIT_ERROR)

            if chksum != '.':
                chksum =  int(chksum)
                chksum_on_file_system = pycksum.cksum(open(path, 'rb'))
                if bytes !=  bytes_on_file_system:
                    print(f'Error: chksum of file from url {url} does not match (expected {chksum}  got {chksum_on_file_system})', file=sys.stderr)
                    print('Exiting..', file=sys.stderr)
                    sys.exit(EXIT_ERROR)

        print(file=sys.stderr)
        print('All OK', file =sys.stderr)
