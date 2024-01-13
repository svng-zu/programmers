def solution(priorities, location):
    answer = 0
    rank = []
    while sum(priorities) != -1*len(priorities) :
        for i in range(len(priorities)) :
            if max(priorities) == priorities[i] and max(priorities) != -1  :
                rank.append(i)
                priorities[i] = -1
                
    for i in range(len(rank)) :
        if rank[i] == location :
            answer = i+1
    return answer