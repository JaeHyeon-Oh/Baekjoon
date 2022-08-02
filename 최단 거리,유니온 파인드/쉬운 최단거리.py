import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
d=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
q=deque()
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(a,b):
    q.append((a,b))
    d[a][b]=3
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=visited[x][y]+1
                    d[nx][ny]=3
                    q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if d[i][j]==2:
            bfs(i,j)
            break

for i in range(n):
    for j in range(m):
        if d[i][j]==1 and not visited[i][j]:
            visited[i][j]=-1

for a in visited:
    print(*a)