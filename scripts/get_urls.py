import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as fh:
        next(fh)
        for line in fh:
            print(line.split()[0])
