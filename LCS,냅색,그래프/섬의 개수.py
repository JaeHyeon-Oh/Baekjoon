import sys
sys.stdin=open('D:/Baekjoon/input.txt')

def dfs(y,x):
    if 0<=y<h and 0 <= x < w:
        if arr[y][x] == 1:
            arr[y][x]=2
            dfs(y-1,x-1)
            dfs(y-1,x)
            dfs(y-1,x+1)
            dfs(y,x-1)
            dfs(y,x+1)
            dfs(y+1,x-1)
            dfs(y+1,x)
            dfs(y+1,x+1)
            return True
        return False


while 1:
    cnt = 0
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    arr=[list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)
