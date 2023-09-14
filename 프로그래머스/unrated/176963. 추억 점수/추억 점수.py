def solution(name, yearning, photo):
    answer = []
    dict_score = { name : value for name, value in zip(name, yearning)}
    
    for i in range(len(photo)):
        cnt = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dict_score.keys():
                cnt += dict_score[photo[i][j]]
        answer.append(cnt)

        
    return answer