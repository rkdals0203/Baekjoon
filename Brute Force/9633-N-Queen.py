ans = 0
n = int(input())
v_row=[0]*n
v_col=[0]*n
v_down_dig=[0]*(2*n)
v_up_dig=[0]*(2*n)

def dfs(depth):
    global ans
    # 종료 조건
    if depth == n:
        ans += 1
        return
    for i in range(n):
        if v_row[depth]==0 and v_col[i]==0 and v_down_dig[depth-i]==0 and v_up_dig[depth+i]==0:
          v_row[depth]=1 
          v_col[i]=1
          v_down_dig[depth-i]=1
          v_up_dig[depth+i]=1
          dfs(depth + 1)
          v_row[depth]=0
          v_col[i]=0
          v_down_dig[depth-i]=0
          v_up_dig[depth+i]=0

dfs(0)
print(ans)
