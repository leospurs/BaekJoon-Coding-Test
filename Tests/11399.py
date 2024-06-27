# 11399 - ATM
n = int(input())
array = list(map(int,input().split()))

# 최소 대기시간 -> 대기시간이 짧은 순서대로 정렬하는것이 가장 짧은 총 대기시간을 제공한다.
array.sort()

result = 0

for i in range(1,n+1):
    result += sum(array[0:i])

print(result)