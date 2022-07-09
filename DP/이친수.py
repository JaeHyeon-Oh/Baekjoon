import sys
sys.stdin=open('D:/Baekjoon/input.txt')

n = int(sys.stdin.readline())
s = [1, 1]
for i in range(2, n):
    s.append(s[i - 2] + s[i - 1])

print(s[n-1])