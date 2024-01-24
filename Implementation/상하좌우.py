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
