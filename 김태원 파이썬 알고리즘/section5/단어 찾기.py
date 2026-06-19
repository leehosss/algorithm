import sys
sys.stdin = open("input.txt","r")
from collections import deque


n = int(input())

d = {}

for i in range(n):
    a = input()
    d[a] = 1
for i in range(n-1):
    a = input()
    d[a] = 0
for x,y in d.items():
    if y == 1:
        print(x)
        break