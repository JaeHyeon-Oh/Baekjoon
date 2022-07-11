#파이썬 1초에 2000만번 계산. 해당 문제 n=100만이므로 시간복잡도(nlogn)인 경우만 가능
import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
dp=[0]
for i in a:
    if dp[-1]<i:
        dp.append(i)
    else:
        left,right=0,len(dp)

        while left <right:
            mid=(left+right)//2
            if dp[mid]<i:
                left=mid+1
            else:
                right=mid
        dp[right]=i
print(len(dp)-1)