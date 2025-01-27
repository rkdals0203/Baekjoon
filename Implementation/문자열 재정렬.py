s = list(input())
s.sort()
num = 0
count = 0

for i in range(len(s)):
    if '0' <= s[i] <= '9':  # 숫자만 판별
        num += int(s[i])
        count += 1

result = ''.join(s[count:]) + str(num)  # 알파벳 부분과 숫자 합계를 합침
print(result)