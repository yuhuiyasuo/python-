import sys


a = []
b = a
print(sys.getrefcount(a))
a = []
print(sys.getrefcount(a))