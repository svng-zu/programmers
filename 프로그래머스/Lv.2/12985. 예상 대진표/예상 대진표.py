def solution(n,a,b):
    answer = 1


    a = a//2 + a%2 #조
    b = b//2 + b%2 #조
    
    while a != b :
        a = a//2 + a%2 #조
        b = b//2 + b%2


        
        answer += 1
    
    return answer