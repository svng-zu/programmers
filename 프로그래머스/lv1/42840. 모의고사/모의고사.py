def solution(answers):
    answer = []
    list_1 = [1,2,3,4,5] #5를 주기로 반복
    list_2 = [2,1,2,3,2,4,2,5] 
    list_3 = [3,3,1,1,2,2,4,4,5,5] #두번씩 반복
    
    score = [0, 0, 0]     
    for i, ans in enumerate(answers) :
        if ans == list_1[i%5] :
            score[0] += 1
        if ans== list_2[i%8] :
            score[1] += 1
        if ans == list_3[i%10] :
            score[2] += 1
    
    
       
    max_score = max(score)
    for j,sco in enumerate(score) :
        if sco == max_score :
            answer.append(j+1)
        
            
    return answer