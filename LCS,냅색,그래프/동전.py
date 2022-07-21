import sys
sys.stdin=open('D:/Baekjoon/input.txt')
t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    coin=list(map(int,sys.stdin.readline().split()))
    m=int(sys.stdin.readline())
    d = [0] *(m+1)
    d[0]=1
    for j in coin:
        for z in range(j,m+1):
            d[z]=d[z]+d[z-j]
print(d[m])