import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
m,n,h=map(int,sys.stdin.readline().split())
q=deque()
tomato=[[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                q.append((i,j,k))
def bfs():
    while q:
        x,y,z=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]

            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if tomato[nx][ny][nz]==0:
                    tomato[nx][ny][nz]=tomato[x][y][z]+1
                    q.append((nx,ny,nz))

bfs()
m=0
flag=0
for i in tomato:
    for j in i:
        for k in j:
            if m<k:
                m=k
                continue
            if k==0:
                flag=1

if flag:
    print(-1)
else:
    print(m-1)