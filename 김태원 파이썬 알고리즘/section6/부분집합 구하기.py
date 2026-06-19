def DFS(l):
    if l == n+1:
        for i in range(n):
            if ch[i] == 1:
                print(i, end = "")
        print()
    else:
        ch[l] =1
        DFS(l+1)
        ch[l] = 0
        DFS(l+1)
        
if __name__=="__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)
    