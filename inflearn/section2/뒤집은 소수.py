import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

def isPrime(x):
    ch= [0]*(x+1)
    if x == 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def reverse(x):
    res = 0
    while x >0:
        res = res*10 + x%10
        x //= 10        
    return res

for i in a:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end = ' ')
         