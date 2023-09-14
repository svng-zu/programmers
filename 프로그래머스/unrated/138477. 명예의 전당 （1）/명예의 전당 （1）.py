def solution(k, score):
    answer = []
    legend = []
    for i in range(len(score)) :
        if i < k :
            legend.append(score[i])
            legend.sort()
            answer.append(legend[0])
        if i >= k: 
            if score[i] > legend[0] :
                legend.sort()
                legend.pop(0)
                legend.append(score[i])
                legend.sort()
                answer.append(legend[0])
            else : 
                answer.append(legend[0])
    
    return answer