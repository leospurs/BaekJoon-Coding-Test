n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

#dictionary를 활용한 탐색
#1. dictionary 선언
dict = {}

#2. 제시된 카드의 키값을 0으로 초기화
for i in m_list:
    dict[i] = 0
#3. 상근이의 카드가 제시된 카드에 있다면, 키의 값을 1로 초기화
for i in n_list:
    if i in dict:
        dict[i] = 1
#4. 출력
for i in dict:
    print(dict[i],end=" ")