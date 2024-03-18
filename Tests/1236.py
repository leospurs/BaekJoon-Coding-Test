# 1236 - 성 지키기

n,m = map(int,input().split())

array = []

# 현재 배열의 행과 열에 필요한 경비원의 최소값을 구하기 위한 배열 생성
# 행과 열의 X 포함 여부를 확인하기 위한 배열이다.
row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        # 2차원 배열에 X가 포함되어있으면, 해당 행과열에 1을 대입
        if array[i][j] == 'X':
            row[i] = 1
            col[j] = 1
            
row_cnt = 0
for i in range(n):
    if row[i] == 0:
        row_cnt += 1
col_cnt = 0      
for i in range(m):
    if col[i] == 0:
        col_cnt += 1
        
# 두 값중 큰 값을 print(작은값을 print하면, 공백이 있는 행/열이 존재할 수 있다.)
print(max(row_cnt, col_cnt))