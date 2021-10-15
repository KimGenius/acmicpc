# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
map = []
for i in range(0, 4):
	userInput = input()
	mapItem = userInput.split()
	map.append(mapItem)

x = 3
y = 3

result = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 1]
]

def clear():
	global x
	global y
	global result
	x = 3
	y = 3
	result = [
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 1]
	]

while(True):
	if x == 0 and y == 0:
		break
	if x == 0:
		if map[y-1][x] == '1':
			y -= 1
			result[y][x] = 1
			continue
		else:
			map[y][x] = '0'
			clear()
			continue
	x -= 1
	isX = map[y][x] == '1'
	if isX:
		result[y][x] = 1
		continue
	else:
		x += 1
		y -= 1
		isY = map[y][x] == '1'
		if isY:
			result[y][x] = 1
			continue
		else:
			y += 1
# 결과를 그리자
for x in result:
	for y in x:
		print(' ', end = '')
		print(y, end = ' ')
	print()
# print(result)
