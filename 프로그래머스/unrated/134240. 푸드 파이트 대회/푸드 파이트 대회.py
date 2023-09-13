def solution(food):
    answer = ''
    half_ans = ''

    print(food)
 
    for j in range(1, len(food)) :
        half_ans += str(j) * int(food[j]/2)
    answer += half_ans + '0' + half_ans[::-1]
    return answer