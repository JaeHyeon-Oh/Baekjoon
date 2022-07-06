import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n, m = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for x in range(n)]
a.sort()
start = 0
end = 1
result=max(a)
while start < n and end < n:
    minus = a[end] - a[start]
    if minus == m:
        result = minus
        break
    elif minus > m:
        if minus <= result:
            result=minus
        start += 1
    else:
        end += 1

print(result)
