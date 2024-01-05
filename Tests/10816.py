import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

dict = {}

for i in n_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
for i in m_list:
    if dict.get(i) == None:
        print(0,end=" ")
    else:
        print(dict.get(i), end = " ")