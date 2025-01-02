array = [1,231,13,2,3,4,5,6,7,8,9,10] #len(array) == 12
indexes = [0]*(max(array)+1) #232개의 0배열
sorted_arr = []

for i in range(len(array)): #0부터 11까지
    index = array[i]
    indexes[index] += 1
    
for j in range(len(indexes)): #11
    if indexes[j] != 0:
        sorted_arr.append(j)

print(sorted_arr)