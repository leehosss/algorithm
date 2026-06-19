import sys
sys.stdin = open("input.txt","r")
from collections import deque

n, k = map(int, input().split())
q = list(range(1,n+1))
dq = deque(q)

while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.pop()