# 이것이 코딩테스트다 - ch.03 그리디_큰수의법칙

n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

first = data[n-1]
second = data[n-2]
result = 0

count_first = (m // k) * k * first
count_second = (m % k) * second

print(count_first + count_second)
