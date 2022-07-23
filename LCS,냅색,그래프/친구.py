import sys
from collections import deque

sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
arr=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
q=deque()

def bfs(x):
    visited = [0] * (n + 1)
    visited[x]=1
    q.append([x,0])
    cnt=0

    while q:
        u,c=q.popleft()
        if c>=2:
            continue

        for i in range(n):
            if not visited[i] and arr[u][i]=="Y":
                visited[i]=1
                q.append([i,c+1])
                # print(i,q,visited)
                cnt+=1
    return cnt
result=[]
for i in range(n):
    result.append(bfs(i))
print(max(result))

