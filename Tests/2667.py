import sys

# 상 , 하 , 좌 , 우 방향 정의
dx = [-1 , 1 , 0 , 0]
dy = [0 , 0 , -1 , 1]
            
def dfs(x,y):
    result = 1 # 원소의 개수
    
    #인접한 원소의 위치확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나는 경우 무시
        if nx <= -1 or nx >= n or ny <= -1 or ny >=n:
            continue
        
        # 처음 방문하는 경우
        if graph[nx][ny] == 1:
            graph[nx][ny] = -1
            result += dfs(nx,ny)
    return result
    
n = int(sys.stdin.readline())
graph = [[0] * n for _ in range(n)] # 2차원 맵
for i in range(n):
    row = input()
    for j in range(n):
        graph[i][j] = int(row[j])
        
# 단지의 수 계산
answer = []
for i in range(len(graph)):
    for j in range(len(graph)):
        # 첫 방문일 경우 dfs 수행
        if graph[i][j] == 1:
            graph[i][j] = -1 # 방문처리
            answer.append(dfs(i,j))

print(len(answer))
answer.sort()

for i in answer:
    print(i)