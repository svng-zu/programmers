def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            # 배열의 끝까지 탐색한 경우, 현재까지의 합이 타겟 넘버와 같으면 1을 반환
            return 1 if current_sum == target else 0
        else:
            # 현재 원소를 더하고 빼는 경우의 수를 재귀적으로 계산
            return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    return dfs(0, 0)