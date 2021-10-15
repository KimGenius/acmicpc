# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
@description
		로봇 방문 순서에 따라 배열 m을 채워주는 함수

@param m	로봇 방문 순서를 저장할 r행 c열의 배열, m[i][j] := (i행 j열)칸의 로봇의 방문 순서 번호
@param r	행의 수 
@param c	열의 수 
"""
def simulate(m, r, c):
	#begin of function
	nowR = 0
	nowC = 0
	index = 1
	for i in range(0, 1):
		for j in range(0, c):
			if m[i][j] == 0:
				m[i][j] = index
				index += 1
				nowC = j
				nowR = i
	while True:
		for j in range(nowC, c):
			for i in range(nowR, r):
				if m[i][j] == 0:
					m[i][j] = index
					index += 1
					nowC = j
					nowR = i
		for i in range(nowR, r):
			for j in range(nowC, -1, -1):
				if m[i][j] == 0:
					m[i][j] = index
					index += 1
					nowC = j
					nowR = i
		for j in range(nowC, c):
			for i in range(nowR, -1, -1):
				if m[i][j] == 0:
					m[i][j] = index
					index += 1
					nowC = j
					nowR = i
		if index >= r * c:
			break;
	#end of function


"""
메인 함수에는 테스트케이스와 입출력에 대한 기본적인 뼈대 코드가 작성되어 있습니다. 
상단의 함수만 완성하여도 문제를 해결할 수 있으며, 
메인 함수를 제거한 후 스스로 코드를 모두 작성하여도 무방합니다.
단, 스스로 작성한 코드로 인해 발생한 에러 등은 모두 참가자에게 책임이 있습니다.
"""
if __name__ == "__main__":
	#테스트케이스의 수를 입력받는다 
	case_num = int(input())

	#각 테스트케이스에 대해 순서대로 데이터를 입력받고 정답을 출력한다 
	for case_index in range(1, case_num+1):

		#행과 열의 수를 입력받는다 
		r, c = [ int(e) for e in input().split() ]

		# 0으로 초기화 된 r행 c열의 리스트를 생성한다 
		m = [ [0] * c for row_index in range(r) ] 

		#주어진 함수를 실행하여 각 칸을 로봇 청소기가 방문하는 순서를 리스트에 저장한다
		simulate(m, r, c)

		#케이스 번호를 출력한다 
		print('Case #%d' % case_index)

		#각 칸의 방문 순서를 출력 형식에 맞게 출력한다
		for i in range(r):
			print(*m[i], sep=' ')