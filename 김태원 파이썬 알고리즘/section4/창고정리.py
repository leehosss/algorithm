import sys
sys.stdin = open("input.txt","r")


n = int(input())
a = list(map(int,input().split()))
m = int(input())
for i in range(m):
    a.sort(reverse = True)
    a[0] -=1
    a[n-1] +=1
a.sort(reverse = True)
print(a[0]-a[n-1])
    
