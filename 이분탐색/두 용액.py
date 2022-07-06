import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
a.sort()

start=0
end=n-1
result=sys.maxsize
while start<end:
    m=a[end]+a[start]
    if abs(m)<result:
        r1=start
        r2=end
        result=abs(m)

    if m>0:
        end-=1
    elif m<0:
        start+=1
    else:
        break
print(a[r1],a[r2])
