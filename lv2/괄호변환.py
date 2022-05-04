def check_valance(p):
	# 괄호 갯수가 같은지 체크
	# 앞에서부터 괄호 갯수가 같은 최소 길이로 잘라서 
	# 문자열 두개로 분리
	a = 0
	b = 0
	for i in range(len(p)):
		if p[i] == '(':
			a += 1
		else:
			b += 1
		if a == b:
			return p[0:a+b], p[a+b:]
	return p, ""

def check_correct(p):
	# 괄호가 올바로 매칭되는지 체크
	# 스택에 넣고 빼고 해서 스택에 최종 남은게 없으면 올바른 괄호
	stackk = []
	for i in p:
		if len(stackk) == 0:
			stackk.append(i)
		else:
			if i == ')' and stackk[len(stackk) - 1] == '(':
				stackk.pop()
			else:
				stackk.append(i)
	if len(stackk) == 0:
		return True
	return False

def solve(answer, p):
	u, v = check_valance(p)
	# u 문자열이 비어있으면 현재 answer 를 리턴
	if u == "":
		return answer

	# u 문자열이 올바른 괄호이면
	if check_correct(u):
		answer += u # u 를 answer 에 붙이고
		u = v
		return solve(answer, v) # v를 다시 체크

	# u 문자열이 올바르지 않으면
	# v 문자열을 올바른지 체크하여 괄호 안에 추가
	res = '(' + solve('', v) + ')'
	# u 문자열은 앞 뒤로 하나씩 떼고 괄호 뒤집기
	u = u[1:len(u) - 1]
	ch = ''
	for i in range(len(u)):
		if u[i] == '(':
			ch += ')'
		else:
			ch += '('
	return answer + res + ch


def solution(p):
	answer = ''
	if p == '':
		return ''

	answer = solve('', p)

	return answer

print(solution("()))((()")) # ()(())()