n = int(input())
coins = list(map(int,input().split()))
coins.sort()

answer = 0
sum = 0
for i in coins:
    if sum + 1 < i:
        answer = sum + 1
    else:
        sum += i
    answer = sum + 1
print(answer)

    
