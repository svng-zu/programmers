def solution(n):
    n_1 = 0
    n_2 = 1
    for i in range(2, n+1) :
        n_1 , n_2 = n_2, n_1+n_2
    return n_2%1234567