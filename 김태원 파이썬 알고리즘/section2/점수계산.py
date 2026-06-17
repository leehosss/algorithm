import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = list(map(int, input().split()))

score = 0
cnt = 0
for i in a:
    if i == 1:
        cnt+=1
        score += cnt
    else:
        cnt = 0
print(score)