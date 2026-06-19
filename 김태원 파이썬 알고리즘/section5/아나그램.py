import sys
sys.stdin = open("input.txt","r")
from collections import deque


a = input()
b = input()

a = list(a)
b = list(b)

a.sort()
b.sort()

if a == b:
    print("YES")
else:
    print("NO")