import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
visited[1]=1
cnt=0

for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(n):
    q.append(n)
    visited[n]=1

    while q:
        x=q.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i]=visited[x]+1
                q.append(i)

q=deque()
bfs(1)
print(len([x for x in visited if 2<=x<=3]))