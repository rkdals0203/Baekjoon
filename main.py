array = [10,5,4,3,1,9,7,8,6,2]

for i in range (1, len(array)):
    for j in range (i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] =array[j-1], array[j]
        else:
            break

print(array)