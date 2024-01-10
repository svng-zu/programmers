def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        num = n
        while num > 0 :
            num -= i
            i += 1
            if num == 0 :
                answer += 1
    
    
    return answer