# 1913 - 회의실 배정

N = int(input())

# 튜플 형태로 입력 받기 위한 리스트
rooms = [tuple(int,input().split()) for _ in range(N)]

# 회의의 최대 개수를 구하기 위해 강의종료시간을 기준으로 리스트 오름차순 정렬
rooms.sort(key=lambda x : (x[1],x[0]))

# 출력값을 받기 위한 변수
result = 1

# 현재 강의 종료시간을 저장하기 위한 변수
end = rooms[0][1]

for i in range(1,N):
    # 선택된 강의의 시작 시간이 현재 강의 종료 시간보다 같거나 뒤의 시간이면
    # end에 저장하고 계속 탐색
    if rooms[i][0] >= end:
        end = rooms[i][1]
        result += 1

print(result)


