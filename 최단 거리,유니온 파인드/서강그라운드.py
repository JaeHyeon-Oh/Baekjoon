import sys
from math import inf
import heapq
sys.stdin=open('D:/Baekjoon/input.txt')
n,m,r=map(int,sys.stdin.readline().split())
t=list(map(int,sys.stdin.readline().split()))
dist=[[]*(n+1) for _ in range(n+1)]
for _ in range(r):
    x,y,z=map(int,sys.stdin.readline().split())
    dist[x].append((y,z))
    dist[y].append((x,z))
def dijk(a):
    visited=[inf]*(n+1)
    heap=[]
    heapq.heappush(heap,(0,a))
    visited[a]=0

    while heap:
        di,node=heapq.heappop(heap)
        for next,d in dist[node]:
            cost=di+d
            if cost<visited[next]:
                visited[next]=cost
                heapq.heappush(heap, (cost, next))
    return visited
result = 0
for i in range(1,n+1):
    re=dijk(i)
    r=0
    for j in range(1,n+1):
        if re[j]<=m:
            r+=t[j-1]
    if result<r:
        result=r
print(result)