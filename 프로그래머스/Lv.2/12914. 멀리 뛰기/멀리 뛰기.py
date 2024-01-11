def solution(n):
    answer = 0
    n_1 = 0
    n_2 = 1
    
    for i in range(n) :
        n_1 , n_2 = n_2, n_1+n_2
        
    answer = n_2 % 1234567
    return answer


        