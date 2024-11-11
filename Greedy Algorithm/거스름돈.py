n = int(input())
changes = [500, 100, 50, 10]
result = 0
for i in changes:
  while (
      n >= i):  #사실 while은 필요가 없다. 왜냐하면 n을 n을 i로 나눈 나머지로 설정하기 때문에 더 나눠질 여지는 없음.
    result += n // i
    n = n % i
print(result)
