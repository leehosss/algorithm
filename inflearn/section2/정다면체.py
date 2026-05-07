import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline



n,m = map(int, input().split())
a = [0]* (n+m+3)
max1 =0
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i+j] +=1
for i in range(1, n+m+1):
    if a[i] >max1:
        max1 = a[i]
for i in range(1, n+m+1):
    if a[i] == max1:
        print(i, end = ' ')
