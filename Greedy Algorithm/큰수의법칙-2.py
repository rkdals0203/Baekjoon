n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
first = numbers[0]
second = numbers[1]
result = 0

moks = m // k
nameoji = m % k
su = m - nameoji

result += first * su
result += second * nameoji
print(result)
