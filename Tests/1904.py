# 1904 - 01 타일
# 동적프로그래밍

num = int(input())

# 최대 입력 길이의 배열 생성
dp = [0] * 1000001

# 점화식에 필요한 요소 적재
dp[1] = 1
dp[2] = 2

for i in range(3,num+1):
    # 점화식 - 피보나치수열
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
    
print(dp[num])