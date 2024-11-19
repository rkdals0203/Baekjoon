n = int(input())
coins = list(map(int, input().split()))
coins.sort()
res = 0

#동전의 최솟값이 1보다 큰 경우는 1을 만들 수 없으므로 답이 1
if coins[0]>1:
    res = 1
#동전의 최솟값이 1부터 시작하는 경우는 따져봐야지..
else:
    sum = coins[0] #최솟값으로 초기화
    for i in range(len(coins)-1):
        #작은 애들부터 더한거+1 하면 다음거보다 크거나 같아?
        if sum +1 >= coins[i+1]:
            #그러면 합류시켜
            sum += coins[i+1]
    #반복문 끝나고나서 sum에 1더한게 답
    res = sum+1
print(res)