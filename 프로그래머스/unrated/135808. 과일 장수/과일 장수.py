def solution(k, m, score):
    answer = 0
    score.sort()
    
    n = len(score)
    a = []
    while n >= m :     
        a.append(score[-m])
        for i in range(m) :
            score.pop() #pop()의 시간이 빠르기 때문에 sort를 순서 고려해서 사용
        n -= m

        
    answer = sum(a)*m
    return answer