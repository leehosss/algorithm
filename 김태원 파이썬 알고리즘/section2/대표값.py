import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = list(map(int, input().split()))

mid = round(sum(a)/n)
res = 2147000000
t = 0
c = 0
for i in range(n):
    if abs(mid-a[i]) < res:
        res = abs(mid-a[i])
        t = a[i]
        c = i
for i in range(n):
    if abs(mid-a[i]) == res:
        if a[i] > t:
            t = a[i]
            c = i
print(mid, c+1) 