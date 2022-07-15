import sys
sys.stdin=open('D:/Baekjoon/input.txt')
a=sys.stdin.readline().strip()
b=sys.stdin.readline().strip()
h=len(a)
w=len(b)
d=[[0]*(w+1) for _ in range(h+1)]
mv=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if a[i-1]==b[j-1]:
            d[i][j]=d[i-1][j-1]+1
            if mv<d[i][j]:
                mv=d[i][j]
print(mv)