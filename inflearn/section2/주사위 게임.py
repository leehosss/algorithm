import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


n = int(input())
max = 0
for i in range(n):
    my = 0
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    if a[0] == a[1] == a[2]:
        my = 10000 + a[0]*1000
    elif a[0] == a[1] or a[0] == a[2]:
        my = 1000 + a[0]*100
    elif a[1] == a[2]:
        my = 1000 + a[1]*100
    else:
        my = a[0]*100
    if my > max:
        max = my
print(max)