import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,m=map(int,sys.stdin.readline().split())
s=[[i] for i in range(n+1)]
for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().split())
    if not x:
        s[y]+=s[z]
        s[z]=s[y]
    else:
        if z in s[y]:
            print('YES')
        else:
            print('NO')

