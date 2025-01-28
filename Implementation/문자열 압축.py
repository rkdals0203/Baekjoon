s = input()
s = "ababababcc"
compressed = []

for slice in range(1,len(s)+1): #1~8까지 슬라이스 개수를 키우기 위한 반복문
    sliced = [s[j:j+slice] for j in range(0, len(s), slice)]
    for k in range(len(sliced)):
        index = 0
        if sliced[k-1] == sliced[k]:
            index += 1
        else:
            sliced[k] = str(index) + sliced[k]
    compressed.append(sliced)

print(compressed)