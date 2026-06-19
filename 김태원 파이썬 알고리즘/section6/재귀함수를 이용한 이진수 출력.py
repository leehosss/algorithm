import sys
import heapq as hq
sys.stdin=open("input.txt", "r")

a = int(input())
def DFS(x):
    if x ==0:
        return
    else:
        DFS(x//2)
        print(x%2, end = "")
DFS(a)