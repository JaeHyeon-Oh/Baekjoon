import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a.sort()
d=[1]*101
for i in range(n):
    for j in range(i):
        if a[i][1]>a[j][1]:
            print(i , j , a[i][1], a[j][1])
            d[i]=max(d[i],d[j]+1)
print(n-max(d))
