import sys


def main():
    filename = sys.argv[1]
    file = open(filename, "r")
    contents = file.read()
    file.close()
    result = 0 
    tmp = contents.split(" ")
    for each in tmp:
    	result += int(each)
    return result

if __name__ == '__main__':
    print(main())
