def solution(survey, choices):
    answer = ''
    n = len(choices)
    mbti_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M':0, 'A':0, 'N':0}
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3} # 1: 매우 비동의, 7: 매우 동의
    for i in range(n):
        if choices[i] <= 3:
            mbti_dict[survey[i][0]] += scores[choices[i]]
        elif choices[i] > 4:
            mbti_dict[survey[i][1]] += scores[choices[i]]
    if mbti_dict['R'] >= mbti_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if mbti_dict['C'] >= mbti_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if mbti_dict['J'] >= mbti_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if mbti_dict['A'] >= mbti_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "TR", "TR", "TR"],	[7, 7, 1, 1]))