import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline



n = int(input())
a = list(map(int, input().split()))

b = round(sum(a)/n+0.5)
min = 2147000000
for i in range(n):
    if abs(b-a[i]) < min:
        min = abs(b-a[i])
        c = a[i]
        d = i
for i in range(n):
    if abs(b - a[i]) ==min and a[i] > c:
        c = a[i]
        d = i
print(b, d+1)
        
            
