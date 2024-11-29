#변수 선언 및 입력값 받기
n,m = map(int,input().split())
a, b, dir = map(int,input().split())
gameMap = []

#맵 채우기
for i in range(n):
    gameMap.append(list(map(int,input().split())))
gameMap[a][b] = -1

for j in range(n):
    print(gameMap[j])


def turn_left(direction):
    #북쪽을 보고 있으면
    if direction == 0:
        return 3
    else:
        return direction-1


#4가 되면 뒤로가는 카운트 초기화
dir_count = 0
#이동한 거리 초기화
count = 0

while True:
    print(a,",",b,"direction:",dir)
    #북쪽을 바라보고 있을 때
    if dir == 0:
        #거기에 안가본 육지가 있다면
        if gameMap[a-1][b] == 0:
            gameMap[a-1][b] = -1
            a = a - 1
            dir_count = 0
            count += 1
        else:
            dir = turn_left(dir)
            dir_count += 1
    #동쪽을 바라보고 있을 떄
    elif dir == 1:
        #거기에 육지가 있다면
        if gameMap[a][b+1] == 0:
            gameMap[a][b+1] = -1
            b = b+1
            dir_count = 0
            count += 1
        else:
            dir = turn_left(dir)
            dir_count += 1
    #남쪽을 바라보고 있을 때
    elif dir == 2:
        #거기에 육지가 있다면
        if gameMap[a+1][b] == 0:
            gameMap[a+1][b] = -1
            a = a+1
            dir_count = 0
            count += 1
        else:
            dir = turn_left(dir)
            dir_count += 1
    #서쪽을 바라보고 있을 때
    elif dir == 3:
        #거기에 육지가 있다면
        if gameMap[a][b-1] == 0:
            gameMap[a][b-1] = -1
            b = b-1
            dir_count = 0
            count += 1
        else:
            dir = turn_left(dir)
            dir_count += 1
    
    #네 방향 다 갈 수 있는 곳이 없는 경우 처음 방향 그대로 하고 뒤로가기
    if dir_count == 4:
        #북쪽을 바라보고 있을 때
        if dir == 0:
            #뒤가 바다가 아니라면
            if gameMap[a+1][b] < 1:
                gameMap[a+1][b] = -1
                a = a + 1
                count += 1
                dir_count = 0
            else:
                break
        #동쪽을 바라보고 있을 떄
        elif dir == 1:
            #뒤에가 바다가 아니라면
            if gameMap[a][b-1] < 1:
                gameMap[a][b-1] = -1
                b = b - 1
                count += 1
                dir_count = 0
            else:
                break
        #남쪽을 바라보고 있을 때
        elif dir == 2:
            #뒤에가 바다가 아니라면
            if gameMap[a-1][b] < 1:
                gameMap[a-1][b] = -1
                a = a - 1
                count += 1
                dir_count = 0
            else:
                break
        #서쪽을 바라보고 있을 때
        elif dir == 3:
            #뒤에가 바다가 아니라면
            if gameMap[a][b+1] < 1:
                gameMap[a][b+1] = -1
                b = b + 1
                count += 1
                dir_count = 0
            else:
                break
        
        
print(count)
    
    
        