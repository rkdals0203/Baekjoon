s = input()
s = 'ababbb'
compressed_list = []

for slice in range(1,len(s)):
    sliced = [s[i:i + slice] for i in range(0,len(s),slice)]
    count = 1
    compressed = []
    for j in range(len(sliced)-1):
        if sliced[j] == sliced[j+1]: #현재 원소가 다음 원소랑 같다면 카운트 증가하고 넘김
            count += 1
        else:
            if count == 1: #현재 원소가 다음 원소랑 같지 않은데 카운트가 1이라면
                compressed.append(sliced[j])
            else: #현재 원소가 다음 원소랑 같지 않은데 카운트가 2 이상이라면
                compressed.append(str(count)+sliced[j])
            count = 1
        
    if sliced[-1] == sliced[-2]: #sliced의 마지막 원소가 이전 원소와 같으면
        compressed.append(str(count)+sliced[-1])
    else: #sliced의 마지막 원소가 이전 원소와 다르면
        compressed.append(sliced[-1])
            
    compressed_list.append(compressed)
print(compressed_list)