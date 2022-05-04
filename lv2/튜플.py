import re

# list(map(int, set(re.findall('\d+', s))))
def solution(s):
	answer = []
	arr = []
	i = 1
	row = 0
	while i < len(s) - 1:
		lst = []
		if s[i] == '{': # 괄호 시작 부분 체크
			start = i + 1
			while i < len(s) - 1 and s[i] != '}':
				i += 1 # 괄호 끝나는 부분 체크
			lst = s[start:i].split(',')
			# 문자열로 된 숫자들을 숫자 타입으로 변경
			arr.append(list(map(int, lst)))
			row += 1
		i += 1
	arr.sort(key = lambda x: len(x))
	for a in arr:
		# answer 와 현재 배열을 집합으로 바꿔서
		# 차집합 연산으로 겹치지 않는 원소 구하기
		n = set(a) - set(answer)
		answer.append(n.pop()) # 집합 원소 빼내기

	return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))