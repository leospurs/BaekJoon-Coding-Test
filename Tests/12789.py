n = int(input())
stack = []

n_list = list(map(int,input().split()))
cnt = 1
while n_list:
    if cnt == n_list[0]:
        cnt += 1
        n_list.pop(0)
    else:
        stack.append(n_list.pop(0))
    
    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break
if len(stack) == 0:
    print("Nice")
else:
    print("Sad")

    