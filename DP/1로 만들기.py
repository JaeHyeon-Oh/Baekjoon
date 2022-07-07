import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=[0 for _ in range(n+1)]
for i in range(2,n+1):
    a[i]=1+a[i-1]
    if i%3==0:
        a[i]=min(a[i],a[i//3]+1)
    if i%2==0:
        a[i]=min(a[i],a[i//2]+1)
print(a[n])
