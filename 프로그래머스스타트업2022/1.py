def solution(atmos):
    count = 0
    i = 0
    while i < len(atmos):
        print(count)
        if atmos[i][0] >= 151 and atmos[i][1] >= 76:
            print('1', atmos[i])
            count += 1
            i += 1
            continue
        if atmos[i][0] >= 81 or atmos[i][1] >= 36:
            print('2', atmos[i])
            j = i + 1
            count += 1
            while j < len(atmos) and j <= i + 2 :
                if atmos[j][0] >= 151 and atmos[j][1] >= 76:
                    print('3', atmos[j])
                    j += 1
                    break
                j += 1
            i = j
            continue
        i += 1
        
    return count

print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))
# print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]))