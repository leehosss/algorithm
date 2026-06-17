import sys
sys.stdin = open("input.txt","r")

n = list(range(21))
for i in range(10):
    a,b = map(int, input().split())
    for j in range((b-a+1)//2):
        n[a+j], n[b-j] = n[b-j], n[a+j]
n.pop(0) 
for i in n:
    print(i, end = " ")