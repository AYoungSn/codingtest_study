def solution(id_list, report, k):
	answer = []
	check = {}
	count = {}
	for i in range(len(id_list)):
		check[id_list[i]] = []
		count[id_list[i]] = 0
		answer.append(0)
	
	for i in report:
		# print(i.split()) ['muzi', 'frodo']
		rep = i.split()
		issame = False
		for j in check[rep[0]]:
			if j == rep[1]:
				issame = True
		if not issame:
			count[rep[1]] += 1
			check[rep[0]].append(rep[1])
	print('check: ', check)
	print('count: ', count)
	for i in count: # count 
		if count[i] >= k:
			for j, lst in check.items():
				if i in lst:
					answer[id_list.index(j)] += 1
	return answer

print(solution(["muzi", "frodo", "apeach", "neo"], 
["muzi frodo","apeach frodo","frodo neo","muzi neo",
"apeach muzi"],2))

print(solution(["con", "ryan"], 
["ryan con", "ryan con", "ryan con", "ryan con"], 
3))