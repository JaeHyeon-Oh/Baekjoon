import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
cnt=0
num=[]
a=0
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y]==1:
        global a
        a+=1
        graph[x][y] = 0
        dfs(x, y + 1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)
            num.append(a)
            cnt+=1
            a=0
num.sort()
print(cnt)
for i in num:
    print(i)