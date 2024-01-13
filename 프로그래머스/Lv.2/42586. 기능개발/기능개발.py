def solution(progresses, speeds):
    answer = []
    days = 0
    tmp = 0
    a = 0 
    while len(progresses) > 0 :

        for i in range(0, len(progresses)) :
            progresses[i] += speeds[i]

        
        tmp = 0
        while progresses and progresses[0] >= 100 :
                progresses.pop(0)
                speeds.pop(0)

                tmp += 1

        if tmp != 0 :
            answer.append(tmp)
        
    return answer