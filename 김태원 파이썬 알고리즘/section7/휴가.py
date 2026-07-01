import sys
sys.stdin=open("input.txt", "r")
def DFS(l, s):
    global res
    if l == n:
        res = max(res, s)
        return
    if l > n:
        return
    if l +a[l][0] <= n:
        DFS(l+a[l][0], s+a[l][1])
    DFS(l+1, s)   
if __name__=="__main__":
    n = int(input())
    a = []
    res = 0
    for i in range(n):
        x, y = map(int, input().split())
        a.append((x,y))
    DFS(0, 0)
    print(res)
        
