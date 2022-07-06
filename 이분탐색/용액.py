import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

s,e=0,n-1
result=sys.maxsize
while s < e:
    print(s,e)
    m=a[e]+a[s]
    if abs(m)<result:
        r1=s
        r2=e
        result=abs(m)
    if m>0:
        e-=1
    elif m<0:
        s+=1
    else:
        break
print(a[r1], a[r2])