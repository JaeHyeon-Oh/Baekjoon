import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
q=deque()
graph=[[] for _ in range(n+1)]
visited = [-1] * (n + 1)

for _ in range(1,m+1):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    q.append(v)

    while q:
        x=q.popleft()

        for i in graph[x]:
            if visited[i] ==-1:
                visited[i]=visited[x]+1
                q.append(i)

bfs(a)

if visited[b]==-1:
    print(visited[b])
else:
    print(visited[b]+1)