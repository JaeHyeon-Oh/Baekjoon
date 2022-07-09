import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,k=map(int,sys.stdin.readline().split())
a=[x for x in range(1,n+1)]
b=[y for y in range(1,n-k+1)]
c=[z for z in range(1,k+1)]
x=1
y=1
z=1
for i in a:
   x*=i
for i in b:
    y*=i
for i in c:
    z*=i

print(x//(y*z))
