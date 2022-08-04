import sys
import heapq
from math import inf
sys.stdin=open('D:/Baekjoon/input.txt')
n,m,start=map(int,sys.stdin.readline().split())
arr=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    arr[x].append((y,z))

def distance(s,e):
    heap=[]
    heapq.heappush(heap,(0,s))
    dist = [inf] * (n + 1)

    while heap:
        d,node=heapq.heappop(heap)

        if d>dist[node]:
            continue

        for next,di in arr[node]:
            cost=d+di
            if dist[next]>cost:
                dist[next]=cost
                heapq.heappush(heap, (cost, next))
    return dist[e]

result=0
for i in range(1,n+1):
    if i==start:
        continue
    result=max(distance(start,i)+distance(i,start),result)
print(result)

