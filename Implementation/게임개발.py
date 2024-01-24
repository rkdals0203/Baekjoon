n, m = map(int,input().split()) # 4 4
row, col, dir = map(int,input().split()) # 1 1 0
k = []
arr = []
for _ in range (n):
  arr.append(list(map(int,input().split())))
arr[row][col]=-1
count = 1
turn_time = 0
isNotEndable = True
dcol=[0,1,0,-1] # 북동남서 순
drow=[-1,0,1,0] # 북동남서 순

def turn_left():
  global dir
  global turn_time
  dir -= 1
  if dir == -1:
    dir = 3
  turn_time+=1

while isNotEndable:
  turn_left()
  new_row = row+drow[dir]
  new_col = col+dcol[dir]
  if arr[new_row][new_col]==0:
    row = new_row
    col = new_col
    arr[row][col]=-1
    count+=1
    turn_time = 0
  elif turn_time==4: # 한 바꾸 돌았으면
    new_row = row-drow[dir]
    new_col = col-dcol[dir]
    if arr[new_row][new_col]==0: # 뒤로 갈 수 있다면
      row = new_row
      col = new_col
    else:
      isNotEndable = False
      break

print(count)


