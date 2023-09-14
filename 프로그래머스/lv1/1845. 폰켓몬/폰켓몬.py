def solution(nums):
    answer = 0
    n = len(nums)/2
    n_list = []
    for i in nums :
        if i not in n_list :
            n_list.append(i)
            
    if len(n_list) > n :
        answer = n
    else :
        answer = len(n_list)
    return answer