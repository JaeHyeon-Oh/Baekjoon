import sys
sys.setrecursionlimit(50000)
sys.stdin=open('D:/Baekjoon/input.txt')

n=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
m=0
s=set()
for i in graph:
    for j in i:
        s.add(j)

s=sorted(s)
arr=[[[1]*n for _ in range(n)] for _ in range(len(s))]

for z in range(len(s)):
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=s[z]:
                arr[z][i][j]=0
def dfs(a,b,c):
    if 0<=b<n and 0<=c<n:
        if arr[a][b][c]==1:
            arr[a][b][c]=-1
            dfs(a,b,c-1)
            dfs(a,b,c+1)
            dfs(a,b-1,c)
            dfs(a,b+1,c)
            return True
        return False

result=[]
for z in range(len(s)):
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[z][i][j]==1:
                dfs(z,i,j)
                cnt+=1
    result.append(cnt)
if len(result)==1:
    print(1)
else:
    print(max(result))