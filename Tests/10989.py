import sys

num = int(sys.stdin.readline())
# 계수정렬을 위한 범위 배열 생성
array = [0] * 10001

# 데이터를 입력받고 해당 데이터의 index에 +1 
for i in range(num):
    data = int(sys.stdin.readline())
    array[data] += 1
    
# 해당 index 의 값이 0이 아니면 값만큼 출력
for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)