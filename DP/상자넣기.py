import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
dp=[1]*1001
for i in range(n):
    for j in range(i):
        if a[j]<a[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))