n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()
res = 0

for i in range(len(k)):
    temp = k[i]
    for j in range(i,len(k)):
        if temp != k[j]:
            res+=1
print(res)
