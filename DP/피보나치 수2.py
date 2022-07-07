import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=[0 for _ in range(91)]
a[0]=0
a[1]=1

for i in range(2,n+1):
    a[i]=a[i-1]+a[i-2]
print(a[n])