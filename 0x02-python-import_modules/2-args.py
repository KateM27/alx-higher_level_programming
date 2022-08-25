#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = len(sys.argv) - 1

    if arg == 0:
        print("{} arguments".format(arg))
    elif arg == 1:
        print("{} argument:".format(arg))
    else:
        print("{} arguments:".format(arg))

    for n in range(arg):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
