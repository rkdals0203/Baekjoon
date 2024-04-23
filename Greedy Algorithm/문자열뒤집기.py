s = list(map(int,input()))
count = 0

def flip(start, end): #처음부터 끝까지 연속으로 뒤집기 실행
  global count
  count += 1

start = 0 #시작 인덱스 초기화
standard = s[0]
for i in range(len(s)):
  if s[i-1]!=s[i]: #i가 0일때는 마지막 원소와 첫번째 원소 비교
    if s[i] != s[standard]: #첫 번쨰 원소가 기준과 다를 수는 없음
      start = i
    elif s[i-1] != s[standard]: #마지막 원소가 기준과 다를 때에 flip실행
      end = i-1
      flip(start,end)

print(count)