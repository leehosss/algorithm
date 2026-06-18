import sys
sys.stdin = open("input.txt","r")


n = int(input())
c = []
for i in range(n):
    a, b = map(int, input().split())
    c.append((a,b))
et = 0
cnt = 0
c.sort(key = lambda x: (x[1], x[0]))

for a,b in c:
    if a>=et:
        cnt+=1
        et = b
    
print(cnt)


    
