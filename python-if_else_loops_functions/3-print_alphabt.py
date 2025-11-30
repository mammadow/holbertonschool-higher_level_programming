#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format("".join(chr(i) if (i != 101 and i != 113)\
 else "")), end="")
