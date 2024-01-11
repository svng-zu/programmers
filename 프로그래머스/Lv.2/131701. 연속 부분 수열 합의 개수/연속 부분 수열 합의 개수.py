def solution(elements):
    answer = 0
    s= set()
    len_e = len(elements)
    elements = elements*2
    
    for i in range(len_e) :
        for j in range(len_e) :
            s.add(sum(elements[j:j+i+1]))
    answer = len(s)
    return answer