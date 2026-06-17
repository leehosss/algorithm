import sys
sys.stdin = open("input.txt","r")

n = input()
cnt = 0
res = 0
for i in n:
    if i.isdecimal():
        i = int(i)
        res = 10*res+i
print(res)
for i in range(1, res+1):
    if res%i ==0:
        cnt+=1
print(cnt)
