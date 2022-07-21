import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
visited=[0]*(n+1)
graph=[[] for _ in range(n+1)]
cnt=0

for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n):
    visited[n]=1
    for i in graph[n]:
        if visited[i]==0:
            dfs(i)


dfs(1)

print(visited.count(1)-1)