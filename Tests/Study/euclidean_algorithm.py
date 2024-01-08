#1. 최대공약수 구하기
#   2개의 자연수 a,b에 대하여 a를 b로 나눈 나머지(a>b)를 r이라하면
#   a,b의 최대공약수는 b와 r의 최대공약수와 같다.
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

#2. 최소공배수 구하기
#   최소공배수 L = 최대공약수 G * a * b
def lcd(a,b):
    return (a * b) / gcd(a,b)