# https://www.acmicpc.net/problem/1011
t = int(input())
cases = []
for i in range(0, t):
    cases.append(input())

result = 0
for case in cases:
    x, y = case.split(' ')
    x = int(x)
    y = int(y)
    finish = y - 1
    move = 1
    queue = [move]
    while True:
        if x == finish:
            break
        if x - 1 != finish:
            

result += 1
print(result)
# 푸는중
