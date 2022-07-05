import sys
sys.stdin=open('input.txt')
N=sys.stdin.readline()
A=list(map(int,sys.stdin.readline().split()))
M=sys.stdin.readline()
start=1
end=max(A)

while start<=end:
    mid=(start+end)//2
    b=[x if x<=mid else mid for x in A]
    if sum(b)<=int(M):
        start=mid+1
    else:
        end=mid-1
print(end)
