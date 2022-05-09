def solution(line):
    answer = []
    keyboard = {
        '1': (0, 0), '2': (0, 1), '3': (0,2), '4':(0,3), '5':(0,4),
        '6': (0,5), '7': (0,6), '8': (0,7), '9': (0,8), '0': (0,9),
        'Q': (1,0), 'W': (1, 1), 'E': (1,2), 'R':(1,3), 'T':(1,4),
        'Y': (1,5), 'U': (1,6), 'I': (1,7), 'O': (1,8), 'P': (1,9),
    }
    left = 'Q'
    right = 'P'
    for l in line:
        l_v = abs(keyboard[l][0] - keyboard[left][0])
        l_h = abs(keyboard[l][1] - keyboard[left][1])
        l_distance = l_v + l_h
        r_v = abs(keyboard[l][0] - keyboard[right][0])
        r_h = abs(keyboard[l][1] - keyboard[right][1])
        r_distance = r_v + r_h
        if l_distance < r_distance:
            answer.append(0)
            left = l
            continue
        elif l_distance == r_distance:
            if l_h < r_h:
                answer.append(0)
                left = l
                continue
            elif l_h == r_h:
                if l_v < r_v:
                    answer.append(0)
                    left = l
                    continue
                elif l_v == r_v:
                    if l in ['1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T']:
                        answer.append(0)
                        left = l
                        continue
        answer.append(1)
        right = l
    return answer

print(solution('Q4OYPI'))