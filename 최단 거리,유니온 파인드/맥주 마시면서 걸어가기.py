import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
t=int(sys.stdin.readline())
q=deque()

def bfs(sx,sy):
    q.append((sx,sy))

    while q:
        qx,qy=q.popleft()
        if abs(qx-ex)+abs(qy-ey)<=1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                con_x,con_y=conv[i][0],conv[i][1]
                if abs(qx-con_x)+abs(qy-con_y)<=1000:
                    visited[i]=1
                    q.append((con_x,con_y))
    print('sad')
    return

for _ in range(t):
    n=int(sys.stdin.readline())
    sx,sy=map(int,sys.stdin.readline().split())
    conv=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    ex,ey=map(int,sys.stdin.readline().split())
    visited=[0]*(n)
    bfs(sx,sy)