
def base(num, base):
	res = ''
	while num > 0:
		res += str(num % base)
		num //= base
	
	return res[::-1]

def solution(n, arr1, arr2):
	answer = []
	map1 = [[' '] * n for _ in range(n)]
	for i in range(len(arr1)):
		val = base(int(arr1[i]), 2)
		val2 = base(int(arr2[i]), 2)
		v = len(val) - 1
		j = n - 1
		while v >= 0:
			if val[v] == '1':
				map1[i][j] = '#'
			j -= 1
			v -= 1
		v = len(val2) - 1
		j = n - 1
		while v >= 0:
			if val2[v] == '1':
				map1[i][j] = '#'
			v -= 1
			j -= 1
	print(''.join(map1[0]))
	for m in map1:
		answer.append(''.join(m))
	return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))