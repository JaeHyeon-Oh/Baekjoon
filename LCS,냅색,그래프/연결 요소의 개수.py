import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
visited=[0]*(n+1)
graph=[[] for _ in range(n+1)]
cnt=0
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n):
    visited[n] = 1
    for j in graph[n]:
        if visited[j]==0:
            dfs(j)

for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1

print(cnt)