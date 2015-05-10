import sys
from random import randint


def main():
    filename = sys.argv[1]
    file = open(filename, "w")
    contents = [str(randint(1, 1000)) for i in range(1, int(sys.argv[2]))]
    #for each in contents:
        #file.write(str(each) + " ")
    file.write(" ".join(contents))
    file.close()

if __name__ == '__main__':
    main()
