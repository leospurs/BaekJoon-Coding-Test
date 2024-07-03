# 11439 - 뒤집기
num = input()

one_cnt = 0
zero_cnt = 0

if num[0] == '1':
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(len(num)-1):
    if num[i] != num[i+1]:
            if num[i+1] == '1':
                zero_cnt += 1
            else:
                one_cnt += 1

            
print(min(one_cnt,zero_cnt))