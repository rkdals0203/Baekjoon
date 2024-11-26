n = int(input())
advMap = [0]*(n+1)
for i in range(n+1):
    advMap[i] = [0]*(n+1)
print(advMap)

nowX = 1
nowY = 1

commands = input().split()
for i in commands:
    if i == "L":
        #만약 왼쪽으로 갔을 때 (= x좌표에서 1 빠질 때 = 두 번째 인덱스에서 1 빠질 때) 0이하라면 아무것도 하면 안됨
        if nowX <= 1:
            continue
        else:
            nowX -= 1
    elif i == "R":
        #만약 오른쪽으로 갔을 때 (= x좌표에서 1 더해질 때 = 두 번째 인덱스에서 1 더해질 때) n이상이라면 아무것도 하면 안됨
        if nowX >= n:
            continue
        else:
            nowX += 1
    elif i == "U":
        #만약 위로 갔을 때 (= y좌표에서 1 빠질 때 = 첫 번째 인덱스에서 1 빠질 때) 0이하라면 아무것도 하면 안됨
        if nowY <= 1:
            continue
        else:
            nowY -= 1
    elif i == "D":
        #만약 아래로 갔을 때 (= y좌표에서 1 더해질 때 = 첫 번째 인덱스에서 1 더해질 때) n이상이라면 아무것도 하면 안됨
        if nowY >= n:
            continue
        else:
            nowY += 1
print(nowY, nowX)
    
    
#2
n = int(input())
nowX = 1
nowY = 1

commands = input().split()
for i in commands:
    if i == "L":
        #만약 왼쪽으로 갔을 때 (= x좌표에서 1 빠질 때 = 두 번째 인덱스에서 1 빠질 때) 0이하라면 아무것도 하면 안됨
        if nowX <= 1:
            continue
        else:
            nowX -= 1
    elif i == "R":
        #만약 오른쪽으로 갔을 때 (= x좌표에서 1 더해질 때 = 두 번째 인덱스에서 1 더해질 때) n이상이라면 아무것도 하면 안됨
        if nowX >= n:
            continue
        else:
            nowX += 1
    elif i == "U":
        #만약 위로 갔을 때 (= y좌표에서 1 빠질 때 = 첫 번째 인덱스에서 1 빠질 때) 0이하라면 아무것도 하면 안됨
        if nowY <= 1:
            continue
        else:
            nowY -= 1
    elif i == "D":
        #만약 아래로 갔을 때 (= y좌표에서 1 더해질 때 = 첫 번째 인덱스에서 1 더해질 때) n이상이라면 아무것도 하면 안됨
        if nowY >= n:
            continue
        else:
            nowY += 1
print(nowY, nowX)
    
    
