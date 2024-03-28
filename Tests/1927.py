# 1927 - 최소 힙
# 힙 구조를 쓰기위한 heapq 라이브러리 import
import heapq

num = int(input())
# 힙 리스트 생성
heap = []
# 결과 값을 담을 리스트 생성
result = []
for _ in range(num):
    x = int(input())
    # x가 0일 때
    if x == 0:
        # heap리스트가 비어있을 때, 결과 리스트에 0 을 넣는다.
        if len(heap) == 0:
            result.append(0)
        # heap리스트에 값이 있을 때, heap 리스트에서 값을 삭제하고, 결과 리스트에 넣는다.
        else:
            result.append(heapq.heappop(heap))
    # x가 0이 아닐 때, 힙 리스트에 값을 넣는다.
    else:
        heapq.heappush(heap,x)

for data in result:
    print(data)