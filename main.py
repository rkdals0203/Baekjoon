coordinate = input()
count = 0
x = int(ord(coordinate[0]) - 96)
y = int(coordinate[1])

steps = [[-2,1],[-2,-1],[2,1],[2,-1],[-1,2],[-1,-2],[1,2],[1,-2]]

for i in steps:
    print(x+i[0],y+i[1])
    if 1 <= x+i[0] <= 8 and 1 <= y+i[1] <= 8:
        count+=1
        
print(count)