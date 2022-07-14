import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,s=map(int,sys.stdin.readline().split())
a=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a.sort()
d=[a[0][1]]+[[0]]*n
tmp=[0]*n
m=0
bm=0
for i in range(1,n):
    while a[i][0]-a[m][0]>=s and m<=i:
        if bm<d[m]:
            bm=d[m]
        m+=1
    d[i]=bm+a[i][1]

for i in range(n):
    if bm<d[i]:
        bm=d[i]
print(bm)