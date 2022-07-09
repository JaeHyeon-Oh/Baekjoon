import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=[int(sys.stdin.readline()) for _ in range(n)]+[0 for _ in range(n,10001)]
dp=[0 for _ in range(10001)]
dp[0]=a[0]
dp[1]=a[0]+a[1]
dp[2]=max(a[0]+a[1],a[0]+a[2],a[1]+a[2])

for i in range(3,n):
    dp[i]=max(dp[i-3]+a[i-1]+a[i],dp[i-2]+a[i],dp[i-1])
print(dp[n-1])