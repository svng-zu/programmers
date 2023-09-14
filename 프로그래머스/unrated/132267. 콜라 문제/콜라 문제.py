def solution(a, b, n):
    answer = 0
    cnt = 0 # a개 콜라를 바꾸는 횟수
    while n >= a :
        n -= a
        cnt += 1
        n += b #바꿔준 콜라 개수 만큼 더해주기 
        
    answer = cnt*b
    return answer