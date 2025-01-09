n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

start = 0
end = max(rice_cakes)
mid = 0
res = 0

while start<=end:
    mid = (start + end) // 2
    total = 0 
    for i in rice_cakes:
        if i > mid:
            total += i - mid
    if total == m:
        res = mid
        break
    # 토탈이 목표치를 초과할 경우 일단 결과에 저장하고 한계 올려서 탐색
    elif total > m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)