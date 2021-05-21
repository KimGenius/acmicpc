a = int(input())
b = input()
i = 0
result = 0
for bItem in b[::-1]:
    itemResult = int(bItem) * a # 보여줄 때는 걍 계산한 거 그대로 보여주고
    print(itemResult)
    result += itemResult * 10 ** i # 실제 더할 때는 10의 n승을 곱한 값으로 해줘야함
    i += 1
print(result)
