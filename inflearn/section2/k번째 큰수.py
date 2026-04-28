import sys


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set()
for i in range(n):
    for x in range(i+1, n):
        for j in range(x+1, n):
            b.add(a[i]+a[x]+a[j])
b = list(b)
b.sort(reverse = True)
print(b[k-1])
            
            
