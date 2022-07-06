import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
a=[int(sys.stdin.readline()) for x in range(n)]

start=max(a)
end=sum(a)
mid=(start+end)//2
while start<=end:
    mid=(start+end)//2
    b=mid
    cnt=0
    for i in a:
        if b<i:
            b=mid
            cnt+=1
        b-=i
    if cnt>=m:
        start=mid+1
    else:
        end=mid-1

print(start)