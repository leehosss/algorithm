import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
cnt = 0
res = 0
for i in a:
    if i == 1:
        res += cnt
        cnt+=1
    else: 
        res += cnt 
        cnt =0
print(res)