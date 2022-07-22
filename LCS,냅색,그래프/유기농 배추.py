import sys
sys.stdin=open('D:/Baekjoon/input.txt')
sys.setrecursionlimit(10000)
t=int(sys.stdin.readline())
def dfs(a,b):
    if 0<=a<n and 0<=b<m:
        if arr[a][b]==1:
            arr[a][b]=2
            dfs(a,b-1)
            dfs(a,b+1)
            dfs(a-1,b)
            dfs(a+1,b)
            return True
        return False

for i in range(t):
    cnt=0
    m,n,k=map(int,sys.stdin.readline().split())
    arr=[[0]*m for _ in range(n)]
    for j in range(k):
        c,r=map(int,sys.stdin.readline().split())
        arr[r][c]=1
    for x in range(n):
        for y in range(m):
            if dfs(x,y)==True:
                cnt+=1
    print(cnt)
