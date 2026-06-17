import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    q,w,e = map(int, input().split())
    for i in range(e):
        if w == 0:
            a[q-1].append(a[q-1].pop(0))
        else:
            a[q-1].insert(0, a[q-1].pop())


lt = 0
rt = n
res = 0
for i in range(n):
    for j in range(lt,rt):
        res += a[i][j]
    if i < n//2:
        lt +=1
        rt -=1
    else:
        lt -=1
        rt +=1
print(res)

