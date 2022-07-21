import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,k=map(int,sys.stdin.readline().split())
coin=[int(sys.stdin.readline()) for _ in range(n)]
d=[0]*(k+1)
d[0]=1
for i in coin:
    for j in range(i,k+1):
        d[j]=d[j]+d[j-i]
print(d[k])