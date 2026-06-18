import sys
sys.stdin = open("input.txt","r")

a = input()
stack = []
cnt = 0
for i in range(len(a)):
    if a[i] =="(":
        stack.append(a[i])
    else:
        stack.pop()
        if a[i-1] == "(":
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)

