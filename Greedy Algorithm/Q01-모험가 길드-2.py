n = int(input())
guild = list(map(int,(input().split(" "))))
guild.sort()
res = 0
grp = []

for i in guild:
  grp.append(i)
  if i <= len(grp):
    res += 1
    grp = []

print(res)