import sys
sys.stdin=open('D:/Baekjoon/input.txt')
s1=sys.stdin.readline().strip()
s2=sys.stdin.readline().strip()
s3=sys.stdin.readline().strip()
result=[[[0]*(len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        for z in range(1,len(s3)+1):
            if s1[i-1]==s2[j-1] and s2[j-1]==s3[z-1]:
                result[i][j][z]=result[i-1][j-1][z-1]+1
            else:
                result[i][j][z]=max(result[i-1][j][z],result[i][j-1][z],result[i][j][z-1])
print(result[-1][-1][-1])

