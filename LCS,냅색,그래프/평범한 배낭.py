import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,k=map(int,sys.stdin.readline().split())
backpack=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
d=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        w=backpack[i-1][0]
        v=backpack[i-1][1]
        if j<w:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j-w]+v,d[i-1][j])
print(d[n][k])