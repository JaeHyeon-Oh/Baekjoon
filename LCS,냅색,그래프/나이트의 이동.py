import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
t=int(sys.stdin.readline())
dx=[2,1,-1,-2,-2,-1,1,2]
dy=[1,2,2,1,-1,-2,-2,-1]
def bfs(a,b,c,d,visited):
    q.append((a,b))

    while q:
        x,y=q.popleft()

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx,ny))

            if nx == c and ny == d:
                return

for i in range(t):
    q=deque()
    n = int(sys.stdin.readline())
    visited=[[0]*n for _ in range(n)]
    fx,fy=map(int,sys.stdin.readline().split())
    lx,ly=map(int,sys.stdin.readline().split())
    if fx==lx and fy==ly:
        print(0)
        continue
    else:
        bfs(fx,fy,lx,ly,visited)
        print(visited[lx][ly])