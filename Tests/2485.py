# 가로수
n = int(input())

#가로수들의 위치를 저장한 리스트
n_list = []
for i in range(n):
    n_list.append(int(input()))

#주어진 가로수들의 간격을 저장하기위한 리스트
m_list = []
for i in range(1,len(n_list)):
    m_list.append(n_list[i] - n_list[i-1])

#최대 공약수를 구하기 위한 메소드
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

# 가로수들의 간격의 최대공약수 구하기
# 초항값 선언
g = m_list[0]
for i in range(len(m_list)):
    g = gcd(g, m_list[i])


# 첫번째 가로수와 마지막 가로수 사이에 필요한 가로수 개수 구하기
need_num = ((n_list[n-1] - n_list[0]) // g - 1)
# 현재 첫번째 가로수와 마지막 가로수 사이에 있는 가로수 개수 구하기
current_num = n - 2

result = need_num - current_num
print(result)
