def solution(n, stages):
    failure_rates = []
    res = []
    for i in range(1,n+1):
        failure = 0
        dodal = 0
        for j in stages:
            if i <= j:
                dodal += 1
            if i == j:
                failure += 1
        if(dodal!=0):
            failure_rates.append((i,failure/dodal)) #실패율은 유저 수 나누기 실패한 유저
        else:
            failure_rates.append((i,0)) #실패율은 유저 수 나누기 실패한 유저
    failure_rates = sorted(failure_rates,key=lambda tuple:tuple[1], reverse=True)
    for k in failure_rates:
        res.append(k[0])
    return res
print(solution(7,[3,2,4,5,2]))