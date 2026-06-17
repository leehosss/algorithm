import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
a.insert(0, [0]*n)
a.append([0]*n)
for i in range(n+2):
    a[i].insert(0,0)
    a[i].append(0)
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j] > a[i+dy[k]][j+dx[k]] for k in range(4)):
            cnt+=1
print(cnt)
                
