#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = map(int, sys.argv[1:])
    total = sum(arguments)
    print(total)
