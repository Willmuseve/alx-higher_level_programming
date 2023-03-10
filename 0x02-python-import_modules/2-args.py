#!/usr/bin/python3
if __name__ == "__main__"
    import sys

a = sys.argv[1:]

if len(a) == 0:
    print("0 arguments.")
else:
    print(f"{len(a)} argument{'s' if len(a) > 1 else ''}:")
    for i, x in enumerate(a):
        print(f"{i+1}: {x}")

