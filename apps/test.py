from test2 import square
import time
import sys

parameter=sys.stdin.buffer.read() #.encode('utf-8')
square(int.from_bytes(parameter,byteorder='big'))
