#구현
n = int(input())
directions = list(input().split())
col, row = 1, 1

for dir in directions:
    if dir == 'L' and col > 1:
        col -= 1
    elif dir == 'R' and col < n:
        col += 1
    elif dir == 'U' and row > 1:
        row -= 1
    elif dir == 'D' and row < n:
        row += 1

print(row, col)

#2
import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
routes = [[0]*(n+1) for _ in range (n+1)]
index_now = [1,1]
routes[1][1] = 1

dx = [0,1]
dx_minus = [0,-1]
dy = [1,0]
dy_minus = [-1,0]

for i in arr:
  if i == 'R':
    if index_now[1] + 1 > n:
      continue
    else:
      index_now[1] += 1
  elif i == 'L':
    if index_now[1] - 1 <= 0:
      continue
    else:
      index_now[1] -= 1
  elif i == 'U':
    if index_now[0] - 1 <= 0:
      continue
    else:
      index_now[0] -= 1
  elif i == 'D':
    if index_now[0] + 1 > n:
      continue
    else:
      index_now[0] += 1

print(*index_now)
