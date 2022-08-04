import sys
import heapq
from math import inf
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
first=int(sys.stdin.readline())
graph=[[]*(n+1) for _ in range(n+1)]
visited = [inf] * (n+1)

for i in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    graph[x].append((y,z))
def dij(f):
    heap=[]
    heapq.heappush(heap,(0,f))
    visited[f]=0

    while heap:
        dist,node=heapq.heappop(heap)
        if dist>visited[node]:
            continue
        for i in graph[node]:
            cost=visited[node]+i[1]
            if cost<visited[i[0]]:
                visited[i[0]]=cost
                heapq.heappush(heap,(cost,i[0]))

dij(first)

for i in visited[1:]:
    if i==inf:
        print("INF")
        continue
    print(i)

