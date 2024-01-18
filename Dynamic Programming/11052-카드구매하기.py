from sys import stdin

# 입력 받기
n = int(stdin.readline().strip())  # 3
prices = [0] + list(map(int, stdin.readline().split()))  # 카드팩 가격들

# dp 배열 초기화
dp = [0] * (n + 1)

# 동적 계획법으로 최댓값 찾기
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + prices[j])

# 결과 출력
print(dp[n])
