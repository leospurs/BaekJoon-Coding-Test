n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

#이진 탐색 메소드를 이용한 탐색(시간복잡도 = O(logN))
def binary_search(list,data):
    if len(list) == 1:
        if list[0] == data:
            return 1
        else:
            return 0
    if len(list) == 0:
        return 0
    
    medium = len(list) // 2

    if data == list[medium]:
        return 1
    if data > list[medium]:
        return binary_search(list[medium:],data)
    else:
        return binary_search(list[:medium],data)

n_list.sort()

for i in range(m):
    result = binary_search(n_list,m_list[i])
    print(result, end=" ")
