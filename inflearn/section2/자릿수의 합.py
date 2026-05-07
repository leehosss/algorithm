import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


max = -2147000000
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    res = 0
    while x >0:
        res += x%10
        x //= 10
    return res
 
for i in range(n):
    if digit_sum(a[i]) > max:
        max = digit_sum(a[i])
        b = a[i]

print(b)
