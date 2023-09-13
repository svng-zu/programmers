def solution(s):
    answer = []
    s_dict = dict()
    
    for i in range(len(s)) :
        if s[i] not in s_dict :
            answer.append(-1) #처음 들어가는 글자는 -1값을 유발
        else :
            answer.append(i-s_dict[s[i]]) #현재의 글자 인덱스에 최근에 들어간 s[i]의 인덱스 값을 뺌
        s_dict[s[i]] = i #s[i]의 인덱스를 value로 dict에 집어넣음
    print(s_dict)
    return answer