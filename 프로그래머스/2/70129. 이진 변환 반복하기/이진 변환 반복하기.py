def solution(s):
    answer = []
    zero = 0
    time = 0    
    tmp = 0
    slen = 0
    while ( len(s) > 1) :
        tmp = s.count('0')
        zero += tmp
        slen = len(s) - tmp
        
        tmps = ""
        while slen > 0 :
            tmps = str(slen%2) + tmps
            slen//=2
            
        time += 1
        s = tmps

        
    
    answer.append(time)
    answer.append(zero)
    return answer