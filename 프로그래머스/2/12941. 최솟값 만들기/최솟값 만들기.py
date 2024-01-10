def solution(A,B):

    a = sorted(A, reverse=True)
    b = sorted(B)
    answer = 0
    while a :
        answer += a.pop(0) * b.pop(0)

    return answer