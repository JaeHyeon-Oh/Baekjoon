import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
m,n=map(int,sys.stdin.readline().split())
tomato=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
q=deque()

dx=[-1,0,1,0]
dy=[0,1,0,-1]


def bfs():
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tomato[nx][ny]==0:
                    tomato[nx][ny]=tomato[x][y]+1
                    q.append((nx,ny))


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j))
bfs()
m=0
flag=0
for x in tomato:
    for y in x:
        if y==0:
            flag=1
        if m<y:
            m=y
if not flag:
    print(m-1)
else:
    print(-1)