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
  
