import sys
input = sys.stdin.readline

def turn_left():
  global direction
  direction = direction-1
  if direction == -1:
    direction = 3
  

n, m = map(int,input().split())
a,b,direction = map(int,input().split())
da = [-1,0,+1,0]
db = [0,1,0,-1]

game_map = []
for _ in range(n):
  arr = (list(map(int,input().split())))
  game_map.append(arr)
# 맵 구성. 1이 바다, 0이 육지

game_map[a][b] = 1
count = 1
turn_time = 0
movable = True
while movable:
  turn_left() #왼쪽으로 돌아서기
  na = a + da[direction]
  nb = b + db[direction]
  if game_map[na][nb] == 0: #갈 수 있는 경우
    game_map[na][nb] = 1
    a = na
    b = nb
    count += 1
    turn_time = 0
  else: #갈 수 없는 경우, 회전 횟수 1 증가됨
    turn_time += 1
    if turn_time == 4:
      na = a-da[direction]
      nb = b-db[direction]
      if game_map[na][nb] == 0:
        a = na
        b = nb
        turn_time = 0
      else:
        movable = False

print(count)

