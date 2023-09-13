def solution(t, p):
    answer = 0
    list_all = []
    for i in range(len(t)-len(p)+1) :
        a = ''
        num_p = i+len(p)
        a += t[i:num_p]
        list_all.append(a)
    print(list_all)
    for x in list_all :
        if int(x) <= int(p) :
            answer += 1
    return answer