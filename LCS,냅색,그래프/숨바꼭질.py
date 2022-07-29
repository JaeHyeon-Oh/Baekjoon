import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
q=deque()
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(x):
    visited[x]=1
    q.append(x)

    while q:
        a=q.popleft()

        for i in graph[a]:
            if not visited[i]:
                visited[i]=visited[a]+1
                q.append(i)

bfs(1)
m=max(visited)
result=[]
for i in range(1,n+1):
    if visited[i]==m:
        result.append(i)
print(min(result), m-1,len(result))