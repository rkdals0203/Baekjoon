n,m = map(int,input().split())
cards = []
for _ in range (n):
  lst = list(map(int,input().split()))
  min_value = min(lst)
  cards.append(min_value)
max_value = max(cards)
print(max_value)