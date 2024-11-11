loc = input() #a1
row = int(loc[1]) #1
col = int(ord(loc[0])) #a -> ord(a)==97 , b ==98 
count = 0

directions = [[-2,-1],[-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]

for dir in directions:
  next_row = dir[0]+row
  next_col = dir[1]+col
  if next_row>=1 and next_row<=8 and next_col >= 97 and next_col <= 104:
    count+=1

print(count)

#2
import sys
input = sys.stdin.readline

data = input()
coordinate = (ord(data[0])-96,int(data[1]))

moves = [(2,-1),(1,-2),(2,1),(1,2),(-2,-1),(-1,-2),(-2,1),(-1,2)]

count = 0
for move in moves:
  new_x = coordinate[0] + move[0]
  new_y = coordinate[1] + move[1]
  if new_x >0 and new_x<9 and new_y>0 and new_y<9:
    count+=1

print(count)