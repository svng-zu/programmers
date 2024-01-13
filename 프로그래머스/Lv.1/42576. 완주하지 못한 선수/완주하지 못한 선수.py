def solution(participant, completion):
    answer = ''
    name = {}
    for i in participant :
        if i in name :
            name[i] += 1
        else :
            name[i] = 1
    for i in completion :
        if i in name :
            name[i] -= 1
    for i in name :
        if name[i] == 1 :
            answer = i

    return answer