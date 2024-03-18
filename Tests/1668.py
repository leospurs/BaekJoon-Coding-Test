# 1668 - 트로피 진열

# 배열을 파라미터로, 보여지는 트로피 개수를 반환하는 메소드
def ascending(array):
    result = 1
    now = array[0]
    for i in range(1,len(array)):
        # 만약 현재 값이 다음 값보다 작다면, 현재값에 다음 값 할당
        if now < array[i]:
            result += 1
            now = array[i]
            
    return result

num = int(input())
array = []
for i in range(num):
    array.append(int(input))
    
print(ascending(array))
# reverse함수를 이용하여 array 원본 리스트를 역순으로 정렬
array.reverse()
print(ascending(array))