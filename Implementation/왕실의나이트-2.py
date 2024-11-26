coordinate = input()
count = 0
x = int(ord(coordinate[0]) - 96)
y = int(coordinate[1])

def right_up(locX,locY):
    if locX+2 <= 8 and locY-1 >= 1:
        global count
        count+=1
def right_down(locX,locY):
    if locX+2 <= 8 and locY+1 <= 8:
        global count
        count+=1
def left_up(locX,locY):
    if locX-2 >= 1 and locY-1 >= 1:
        global count
        count+=1
def left_down(locX,locY):
    if locX-2 >= 1 and locY+1 <= 8:
        global count
        count+=1
def up_left(locX,locY):
    if locY-2 >= 1 and locX-1 >= 1:
        global count
        count+=1
def up_right(locX,locY):
    if locY-2 >= 1 and locX+1 <= 8:
        global count
        count+=1
def down_left(locX,locY):
    if locY+2 <= 8 and locX-1 >= 1:
        global count
        count+=1
def down_right(locX,locY):
    if locY+2 <= 8 and locX+1 <= 8:
        global count
        count+=1
        
right_up(x,y)
right_down(x,y)
left_up(x,y)
left_down(x,y)
up_left(x,y)
up_right(x,y)
down_left(x,y)
down_right(x,y)

print(count)

#2
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