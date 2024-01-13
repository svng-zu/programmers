from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)

    # 종이 조각으로 만들 수 있는 모든 순열을 구하고 중복 제거
    permutations_set = set(int(''.join(p)) for i in range(1, len(num_list) + 1) for p in permutations(num_list, i))

    # 각 조합이 소수인지 판별
    for num in permutations_set:
        if is_prime(num):
            answer += 1

    return answer


