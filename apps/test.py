from test2 import square
import time
import sys

parameter=sys.stdin.read().encode()
square(int.from_bytes(parameter,byteorder='little'))
