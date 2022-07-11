import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=[0]+list(map(int,sys.stdin.readline().split()))+[0]
dp=[1]*1001
cnt=0
for i in range(1,n+1):
    for j in range(1,i):
        if a[i]<a[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))