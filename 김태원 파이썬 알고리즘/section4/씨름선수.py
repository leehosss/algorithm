import sys
sys.stdin = open("input.txt","r")


n = int(input())
c = []
for i in range(n):
    a, b = map(int, input().split())
    c.append((a,b))
c.sort(reverse = True)
lg = 0
cnt = 0
for a,b in c:
    if b > lg:
        lg = b
        cnt+=1
print(cnt)


    
