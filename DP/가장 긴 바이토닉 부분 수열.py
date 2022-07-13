import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
dp=[1]*n
d=[1]*n
s=[0]*n

for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+1)
a.reverse()

for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            d[i]=max(d[i],d[j]+1)

d.reverse()
print(dp)
print(d)
for i in range(n):
    s[i]=dp[i]+d[i]

print(max(s)-1)

