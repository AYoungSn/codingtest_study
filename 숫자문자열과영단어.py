def solution(s):
    answer = 0
    word = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven':7,
        'eight': 8,
        'nine': 9
    }
    for w in word.items():
        s = s.replace(w[0], str(w[1])) # word의 키값에 해당하는 문자를 전부 숫자로 교체
    return s
print(solution("one4seveneight"))