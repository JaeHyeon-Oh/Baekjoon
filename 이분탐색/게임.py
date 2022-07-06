import sys
sys.stdin=open("D:/Baekjoon/input.txt")
x,y=map(int,sys.stdin.readline().split())
start=1
end=x
target=y*100//x
if target>=99:
    print('-1')
while start<=end:
    mid=(start+end)//2
    c=(y+mid)*100//(x+mid)

    if c<=target:
        start=mid+1
    else:
        end=mid-1
if target <99:
    print(start)
