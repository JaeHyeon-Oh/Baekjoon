import sys
sys.stdin=open('input.txt')
N,M=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
A.sort()

start=min(A)
end=max(A)

while start<=end:
    mid=(start+end)//2
    b=[x-mid for x in A if x>mid]
    if sum(b)>=M:
        start = mid + 1
    else:
        end=mid-1

print(end)