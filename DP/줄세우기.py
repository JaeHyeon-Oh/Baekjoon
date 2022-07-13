import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(int(sys.stdin.readline()) for _ in range(n))
dp=[1]*(n+1)
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))