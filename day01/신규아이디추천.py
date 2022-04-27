from operator import le


def solution(new_id):
	answer = ''
	new_id = new_id.lower()
	for i in new_id:
		if i.isalpha() or i.isdigit() or i == '-' \
			or i == '_' or i == '.':
			answer += i
	new_id = answer
	prev = new_id[0]
	answer = prev
	for i in range(1, len(new_id)):
		if prev == '.' and new_id[i] == '.':
			for j in range(i + 1, len(new_id)):
				if prev == '.' and new_id[j] == '.':
					i = j
				else:
					break
		else:
			answer += new_id[i]
		prev = new_id[i]
	answer = answer.strip('.')
	print(answer)
	if answer == '':
		answer = 'a'
	if len(answer) >= 16:
		answer = answer[:15]
		answer = answer.strip('.')
	while len(answer) <= 2:
		answer += answer[len(answer) - 1]
	return answer

print(solution("...!@BaT#*......y.abcdefghijklm"))