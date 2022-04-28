def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = ''
    keypad = {
        '1': (0,0), '2': (0, 1), '3': (0, 2),
        '4': (1,0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2)
    }
    l_pos = keypad['*']
    r_pos = keypad['#']
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            l_pos = keypad[str(num)]
        elif num in [3, 6, 9]:
            answer += 'R'
            r_pos = keypad[str(num)]
        else:
            l_dis = distance(l_pos, keypad[str(num)])
            r_dis = distance(r_pos, keypad[str(num)])
            if l_dis == r_dis:
                answer += hand[0].upper()
                if hand == 'left':
                    l_pos = keypad[str(num)]
                else:
                    r_pos = keypad[str(num)]
            elif l_dis > r_dis:
                answer += 'R'
                r_pos = keypad[str(num)]
            else:
                answer += 'L'
                l_pos = keypad[str(num)]
    return answer