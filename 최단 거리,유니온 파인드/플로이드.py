import sys
from math import inf
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[]*(n+1) for _ in range(n+1)]
visited=[[inf]*(n) for _ in range(n)]
for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    visited[x-1][y-1]=min(visited[x-1][y-1],z)

for k in range(n):
    visited[k][k]=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]>visited[i][k]+visited[k][j]:
                visited[i][j]=visited[i][k]+visited[k][j]

for i in range(n):
    for j in range(n):
        if visited[i][j]==inf:
            visited[i][j]=0
for i in range(n):
    print(*visited[i])
