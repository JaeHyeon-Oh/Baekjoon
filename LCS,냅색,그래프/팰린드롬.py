import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
a=sys.stdin.readline().strip()
b=a[::-1]
d=[[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i-1]==b[j-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j],d[i][j-1])
print(n-d[-1][-1])