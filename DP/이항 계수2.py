import sys
sys.stdin=open('D:/Baekjoon/input.txt')
n,k=map(int,sys.stdin.readline().split())

def factorial(n):
    if n==0:
        return 1
    result=1
    for i in range(1,n+1):
        result*=i
    return result

print((factorial(n)//(factorial(k)*factorial(n-k)))%10007)
