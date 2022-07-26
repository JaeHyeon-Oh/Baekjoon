import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')

n,m=map(int,sys.stdin.readline().split())
arr=[list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j):
    visited[i][j]=1
    q.append((i,j))

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))

bfs(0,0)
print(visited[n-1][m-1])



