#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 == 0:
        print("{0} arguments.".format(len(argv) - 1))
    else:
        print("{0} {1}:".format(
                            len(argv) - 1, "argument" if len(argv) - 1 == 1
                            else "arguments"))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
