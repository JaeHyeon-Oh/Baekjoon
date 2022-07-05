import sys
sys.stdin=open('input.txt')
N=sys.stdin.readline()
A=list(map(int,sys.stdin.readline().split()))
A.sort()
M=sys.stdin.readline()
input=list(map(int,sys.stdin.readline().split()))


for i in range(int(M)):
    start = 0
    end = int(N) - 1
    while start<=end:
        mid=(start+end)//2
        if A[mid]==input[i]:
            print('1')
            break
        elif A[mid]>input[i]:
            end=mid-1
        else:
            start=mid+1
        if start>end:
            print('0')

