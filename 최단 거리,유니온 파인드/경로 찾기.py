#First
# import sys
# from math import inf
# sys.stdin=open('D:/Baekjoon/input.txt')
#
# n=int(sys.stdin.readline())
# d=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if d[i][j]==0:
#             d[i][j]=inf
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if d[i][j]>d[i][k]+d[k][j]:
#                 d[i][j]=1
#
# for i in range(n):
#     for j in range(n):
#         if d[i][j]==inf:
#             d[i][j]=0
# for i in range(n):
#     print(*d[i])

#Second
# import sys
# sys.stdin=open('D:/Baekjoon/input.txt')
#
# n=int(sys.stdin.readline())
# d=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if d[i][k] and d[k][j]:
#                 d[i][j]=1
#
#
# for i in range(n):
#     print(*d[i])

import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
d=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
q=deque()
check=[[0]*n for _ in range(n)]

def bfs(v):
    q.append(v)
    visited = [0] * n

    while q:
        nx=q.popleft()
        for i in range(n):
            if not visited[i] and d[nx][i]:

                visited[i]=1
                q.append(i)
                check[v][i]=1

for a in range(n):
    bfs(a)

for i in check:
    print(*i)