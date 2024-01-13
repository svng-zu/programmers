def solution(nums):
    answer = 0
    po = {}
    for i in nums :
        if i not in po :
            po[i] = 1
    print(len(po))
    if len(po) < len(nums)/2 :
        answer = len(po)
    else :
        answer = len(nums)/2

            
    return answer