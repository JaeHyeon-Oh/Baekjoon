import sys
sys.stdin=open('D:/Baekjoon/input.txt')

n=int(sys.stdin.readline())
a=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]+[[0]* x for x in range(n,1001)]


for j in range(1,n):
   a[j][0]=min(a[j-1][1],a[j-1][2]) + a[j][0]
   a[j][1]=min(a[j-1][0],a[j-1][2]) + a[j][1]
   a[j][2]=min(a[j-1][1],a[j-1][0]) + a[j][2]
print(min(a[n-1][0],a[n-1][1],a[n-1][2]))