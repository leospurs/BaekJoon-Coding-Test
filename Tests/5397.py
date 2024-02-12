#커서를 기준으로 양 옆으로 스택 2개를 생성하여 문제를 푼다.

test_num = int(input())

for _ in range(test_num):
    test_case = input()
    left_stack = []
    right_stack = []
    for i in test_case:
        if i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif i == '-':
            if left_stack:      
                left_stack.pop()
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))