import sys


def read_multiple_files():
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            filename = sys.argv[i]
            text_file = open(filename, "r")
            text = text_file.read()
            text_file.close()
            print(text)

if __name__ == '__main__':
    read_multiple_files()
