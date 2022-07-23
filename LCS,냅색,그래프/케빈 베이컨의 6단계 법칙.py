import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
q=deque()
result=[]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    visited = [0] * (n + 1)
    q.append(v)
    while q:
        x=q.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i]=visited[x]+1
                q.append(i)
    result.append((v,sum(visited)-visited[v]))

for i in range(1,n+1):
    bfs(i)

result.sort(key=lambda x:x[1])
print((result[0][0]))