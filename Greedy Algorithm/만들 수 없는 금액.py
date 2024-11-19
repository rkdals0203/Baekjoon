n = int(input())
coins = list(map(int, input().split()))
coins.sort()
res = 0
sum = 0

for i in range(len(coins)):
    #작은 애들부터 더한거+1 하면 다음거보다 크거나 같아?
    if sum +1 >= coins[i]:
        #그러면 합류시켜
        sum += coins[i]
#반복문 끝나고나서 sum에 1더한게 답
res = sum+1
print(res)

