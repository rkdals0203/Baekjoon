
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
