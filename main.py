s = list(map(int,input()))
count = 0

def flip(start, end): #처음부터 끝까지 연속으로 뒤집기 실행
  global count
  count += 1
  print(start, end)
  
start = 0 #시작 인덱스 초기화
standard = s[0]
for i in range(1,len(s)):
  if s[i-1]!=s[i]:
    if s[i] != s[standard]:
      start = i
    elif s[i-1] != s[standard]:
      end = i-1
      flip(start,end)

print(count)