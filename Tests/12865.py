# 12865 - 평범한 배낭
# 동적프로그래밍

# 물품의 수 N, 배낭의 무게 K를 받는다.
N,K = map(int,input().split())

# 최대 물건들의 가치합을 계산할 테이블을 생성한다.
dp = [[0] * (K+1) for _ in range(N+1)]

# 물건의 수만큼 무게와 가치를 입력받는다.
for i in range(1,N+1):
    weight, value = map(int,input().split())
    
    # 배낭의 무게가 0인 경우부터 K까지 하나하나 비교한다.
    for j in range(1,K+1):
        # 입력받은 물건의 무게가 현재 배낭의 무게보다 크다면, 이전 최대값을 그대로 받는다.
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 입력받은 물건의 무게가 현재 배낭의 무게보다 작다면, 이전 최대값을 무게와 현재까지의 최대값 중 큰값을 넣는다.
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            
print(dp[N][K])
    