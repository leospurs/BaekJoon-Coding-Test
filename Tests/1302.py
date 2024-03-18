#1302 - 베스트셀러

num = int(input())
#dictionary를 이용하여 입력 값을 받는다.
books = {}

# 이미 책이 dictionary에 있다면, 해당 values에 +1, 아니면 1
for _ in range(num):
    book = input()
    
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

# dictionary의 value값중 가장 큰 값 추출
target = max(books.values())
# 가장 많이 팔린 책을 담을 리스트
array = []

# target값과 value값이 같은 book만 append
for book, number in books.items():
    if number == target:
        array.append(book)
# 베스트 셀러가 2권 이상일 때 문자순으로 정렬 후 가장 앞의 것을 print        
print(sorted(array[0]))