import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=[0]*1001
a[1]=1
a[2]=2
for i in range(3,1001):
    a[i]=a[i-1]+a[i-2]

print(a[n]%10007)
