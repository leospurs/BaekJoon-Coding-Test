# 이것이 코딩테스트다 - ch.03 그리디_숫자카드게임
n,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    
    min_num = min(data)
    
    result = max(result,min_num)
    
print(result)