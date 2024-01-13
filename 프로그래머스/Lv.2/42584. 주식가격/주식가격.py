def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 스택이 비어있지 않고, 현재 주식 가격이 스택의 가장 위의 가격보다 작을 경우
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        
        stack.append(i)

    # 스택에 남아있는 인덱스들은 떨어지지 않은 기간이 끝까지 이어진 경우이므로 처리
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top

    return answer