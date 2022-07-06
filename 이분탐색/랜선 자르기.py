import sys
sys.stdin=open("D:/Baekjoon/input.txt")
k,n=map(int,sys.stdin.readline().split())
a=[int(sys.stdin.readline()) for _ in range(k)]
start=1
end=sum(a)
while start<=end:
    mid=(start+end)//2
    s=[x//mid for x in a]
    if sum(s)>=n:
        start=mid+1
    else:
        end=mid-1
print(end)