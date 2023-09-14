def solution(k, m, score):
    answer = 0
    score.sort()
    n = len(score)
    a = []
    while n >= m :     
        a.append(score[-m])
        for i in range(m) :
            score.pop()
        n -= m

        
    answer = sum(a)*m
    return answer