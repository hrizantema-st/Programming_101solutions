import sys

import os

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except FileNotFoundError as error:
                print(error)
    return total_size


if __name__ == '__main__':
    print(get_size(sys.argv[1]))

