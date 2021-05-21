fix, vari, price = input().split()
fix = int(fix)
vari = int(vari)
price = int(price)

if vari >= price:
    print(-1)
    exit()

total = fix
result = int(fix / (price - vari)) + 1

print(result)
