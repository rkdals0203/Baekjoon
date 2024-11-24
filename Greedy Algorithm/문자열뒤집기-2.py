s = input()
res0 = 0
res1 = 0

if s[0] == "0":
    res0+=1
else:
    res1+=1

for i in range(1,len(s)):
    if s[i] == "0" and s[i-1] == "1":
        res0+=1
    elif s[i] == "1" and s[i-1] == "0":
        res1+=1

    
print(min(res0,res1))