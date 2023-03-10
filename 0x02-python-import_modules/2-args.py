#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    y = len(argv)

    if y == 1:
        z = "arguments."
    elif y == 2:
        z = "argument:"
    else:
        z = "arguments:"
    print("{} {}".format(y - 1, z))
    for i, value in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, value))

