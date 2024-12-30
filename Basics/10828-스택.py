from sys import stdin
n = int(stdin.readline().strip())
stack = []

for i in range(n):
    command = stdin.readline().split()
    if command[0] == 'top':
        print(stack[-1] if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if not stack else 0)
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    else:
        push, num = command[0], command[1]
        stack.append(int(num))
        
        
#2
stack = []
n = int(input())
for i in range(n):
    command = list(input().split())
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print("-1")
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
