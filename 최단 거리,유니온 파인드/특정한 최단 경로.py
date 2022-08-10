import sys
import heapq
from math import inf
sys.stdin=open('D:/Baekjoon/input.txt')
n , e=map(int,sys.stdin.readline().split())
g=[[]*(n+1) for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    g[a].append((b,c))
    g[b].append((a,c))

v1,v2=map(int,sys.stdin.readline().split())

def dijk(start,e):
    heap=[]
    heapq.heappush(heap,(0,start))
    dist = [inf] * (n + 1)
    dist[start]=0
    while heap:
        di,node=heapq.heappop(heap)

        for no,d in g[node]:
            cost=di+d
            if cost<dist[no]:
                dist[no]=cost
                heapq.heappush(heap,(cost,no))
    return dist[e]


total=min(dijk(1,v1)+dijk(v1,v2)+dijk(v2,n), dijk(1,v2)+dijk(v2,v1)+dijk(v1,n))
if total >= inf :
    print(-1)
else : print(total)