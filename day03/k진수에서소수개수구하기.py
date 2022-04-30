import math
def num_base(n, k):
    base = ''
    while n > 0:
        base += str(n % k)
        n = n // k
    return base[::-1]

def solution(n, k):
    answer = 0
    base = num_base(n, k)
    for num in base.split('0'):
        if num == '':
            continue
        n = int(num, 10)
        if n >= 2:
            isPrime = True
            for p in range(2, int(math.sqrt(n)) + 1):
                if n % p == 0 and n != p:
                    isPrime = False
                    break
            if isPrime:
                answer += 1
    return answer

def prime(num):
    if (num == 1):
        return False
    # for p in range(2, num // 2 + 1):
    #     if num % p == 0 and num != p:
    #         return False
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0 and num != i:
            return False
        i += 1
    return True

def solution2(n, k):
    answer = 0
    base = num_base(n, k)
    for num in base.split('0'):
        if num == '':
            continue
        n = int(num, 10)
        if prime(n):
            answer += 1
    return answer

print('#1:', solution(437674, 3))
print('#2:', solution(110011, 10))
print('#3:', solution(11, 10))