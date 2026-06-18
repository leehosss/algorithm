import sys
sys.stdin = open("input.txt","r")



n, m  = map(int, input().split())
a = list(map(int, input().split()))

def count(x):
    cnt = 1
    sum =0
    for i in a:
        if sum+i > x:
            cnt+=1
            sum = i
        else:
            sum+=i
    return cnt

lt = 1
rt = sum(a)
res = 0
maxx = max(a)
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1
print(res)






        
    