# 2217 - 로프
n = int(input())

rope = [int(input()) for _ in range(n)]

# n개의 로프를 사용하여 들수있는 중량 w는 로프가 버틸수있는 최대중량의 최소값 * 로프 개수
rope.sort()

result = []
for i in rope:
    result.append(n * i)
    n -= 1
    
    
print(max(result))