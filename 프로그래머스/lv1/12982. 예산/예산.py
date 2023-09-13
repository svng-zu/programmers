def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    a = 0
    
    for i in range(len(d)) :
        a += d[i]
        if a <= budget :
            answer = i+1

        
    return answer