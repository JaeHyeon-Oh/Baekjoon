import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
q=deque()
bresult=[]

for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[y].append(x)
    graph[x].append(y)


for i in range(1,n+1):
    graph[i].sort()


visited=[0]*(n+1)
dresult = []


def dfs(a):
    visited[a]=1
    dresult.append(a)

    for i in graph[a]:
        if not visited[i]:
            dfs(i)
def bfs(a):
    q.append(a)
    visited=[0]*(n+1)
    visited[a]=1

    while q:
        c=q.popleft()
        bresult.append(c)

        for i in graph[c]:
            if not visited[i]:
                visited[i]=1
                q.append(i)



dfs(v)
print(' '.join(map(str,dresult)))

bfs(v)
print(' '.join(map(str,bresult)))
