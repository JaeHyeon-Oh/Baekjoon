
# from bisect import bisect_left
# import sys
# sys.stdin=open('D:/Baekjoon/input.txt')
# input=sys.stdin.readline
# N = int(input())
# arr = [0] + list(map(int,input().split())) # input
# d = [0] * (N+1) # for memoization
# cmp = [-1000000001] # 이진탐색을 위해 생성.
# maxVal = 0 #최대값을 저장할 변수
#
# for i in range(1, N+1): #arr 반복 실행.
#     if cmp[-1] < arr[i]: #이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교.
#         cmp.append(arr[i])
#         d[i] = len(cmp) - 1
#         maxVal = d[i]
#     else:
#         d[i] = bisect_left(cmp, arr[i]) #현재 값이 어느 위치의 값에 해당하는지 비교.
#         cmp[d[i]] = arr[i] #cmp 업데이트.
# print(maxVal) #최대 길이 출력
#
# res = []
# for i in range(N, 0, -1):
#     if d[i] == maxVal:
#         res.append(arr[i])
#         maxVal -= 1
# res.reverse()
# print(*res)

from bisect import bisect_left
import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
tmp=[-1000000001]
d=[0]*n
res=[]
mv=0
for i in range(n):
    if tmp[-1]<a[i]:
        tmp.append(a[i])
        d[i]=len(tmp)-1
        mv=d[i]
    else:
        d[i]=bisect_left(tmp,a[i])
        tmp[d[i]]=a[i]
print(mv)

for i in range(n-1,-1,-1):
    if d[i]==mv:
        res.append(a[i])
        mv-=1
res.reverse()
print(*res)
