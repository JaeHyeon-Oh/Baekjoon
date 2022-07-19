import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,k=map(int,sys.stdin.readline().split())
coin=[int(sys.stdin.readline()) for _ in range(n)]
d=[10001]*(k+1)
d[0]=0
for i in coin:
    for j in range(i,k+1):
        d[j]=min(d[j],d[j-i]+1)
if d[k]==10001:
    d[k]=-1
print(d[k])