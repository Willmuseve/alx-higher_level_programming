#!/usr/bin/python3

if __name__ == "__main__":
    import sys

args = sys.argv[1:]

if len(args) == 0:
    print("0 arguments.")
else:
    print(f"{len(args)} argument{'s' if len(args) > 1 else ''}:")
    for i, arg in enumerate(args):
        print(f"{i+1}: {arg}")

