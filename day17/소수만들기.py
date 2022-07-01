import itertools
import math

def solution(nums):
    arr = list(itertools.combinations(nums, 3))
    print(arr)
    answer = 0
    for a in arr:
        tmp = sum(a)
        is_sosu = True
        for i in range(2, int(math.sqrt(tmp))+ 1):
            if tmp % i == 0:
                is_sosu = False
                break
        if is_sosu:
            answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))