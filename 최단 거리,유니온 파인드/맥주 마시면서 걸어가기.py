import sys
from collections import deque
sys.stdin=open('D:/Baekjoon/input.txt')
t=int(sys.stdin.readline())
def bfs(x,y):

    q.append((x,y))
    while q:
        px,py=q.popleft()
        if abs(ex - px) + abs(ey - py) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i] and abs(conv[i][0]-px) +abs(conv[i][1]-py)<=1000:
                visited[i]=1
                q.append((conv[i][0],conv[i][1]))

    print('sad')


for _ in range(t):
    q = deque()
    n=int(sys.stdin.readline())
    visited = [0] * (n)
    sx,sy=map(int,sys.stdin.readline().split())
    conv=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    ex,ey=map(int,sys.stdin.readline().split())
    bfs(sx,sy)