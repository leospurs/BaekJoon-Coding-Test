#이진 탐색 학습

#1. 이진탐색(반복분)
def binary_search(list, data):
    list.sort()

    start = 0           #시작 위치
    end = len(list) -1  #마지막 위치

    while start <= end:
        medium = len(list) // 2 #중간값

        if list[medium] == data:
            return medium
        
        elif list[medium] > data:
            end = medium - 1
        else:
            end = medium + 1
    return None
        
#2. 이진탐색(재귀)
# 존재하면 1, 아니면 0 반환
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

