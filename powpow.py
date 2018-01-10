#!/usr/local/bin/python3
import sys
x = int(sys.argv[1])
[print("%s - %s: %s" % (x, len(str(2**(2**x))), 2**(2**x))) for x in range(x)]

