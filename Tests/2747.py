num = int(input())

a,b = 0,1

while num > 0:
    a,b = b, a+b
    num -= 1

print(a)