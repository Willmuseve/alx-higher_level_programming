#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    total = sum(int(sys.argv[x]) for x in range(1, len(sys.argv)))
    print("{}".format(total))
