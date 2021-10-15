if __name__ == "__main__":
	#행과 열의 수를 입력받는다 
	N, M = [ int(e) for e in input().split() ]
	# 버튼 처리
	maps = [ [0] * 1005 for row_index in range(1005) ]
	for i in range(0, N):
		L, R, B, T = [ int(e) for e in input().split() ]
		for btnI in range(L, R + 1):
			for btnJ in range(B, T + 1):
				maps[btnI][btnJ] = i + 1
	result = dict()
	# 클릭 처리
	for i in range(0, M):
		X, Y = [ int(e) for e in input().split() ]
		if maps[X][Y] in result:
			result[maps[X][Y]] += 1
		else:
			result[maps[X][Y]] = 1
	# 출력 처리
	for i in range(1, N + 1):
		if i not in result:
			result[i] = 0
		print('Button #' + str(i) + ': ' + str(result[i]))
