import sys
sys.setrecursionlimit(10000)
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n+1)]


def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x,y):
    nx=find(x)
    ny=find(y)

    if nx==ny:
        return
    if nx<ny:
        parent[nx]=ny
    else:
        parent[ny]=nx

for _ in range(m):
    check,x,y=map(int,sys.stdin.readline().split())
    if check:
        a=find(x)
        b=find(y)
        if a==b:
            print('YES')
        else:
            print('NO')
    else:
        union(x,y)

