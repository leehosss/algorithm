import sys
sys.stdin = open("input.txt","r")

n = input()

res = ""
stack = []

for i in n:

    if i.isdecimal():
        res += i

    else:
        if i == "(":
            stack.append(i)

        elif i in "*/":
            while stack and stack[-1] in "*/":
                res += stack.pop()
            stack.append(i)

        elif i in "+-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(i)

        elif i == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)