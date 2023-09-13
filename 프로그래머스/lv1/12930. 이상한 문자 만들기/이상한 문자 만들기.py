def solution(s):
    list_s = list(s)
    answer = ''
    cnt = 0
    print(list_s)
    for i in range(len(list_s)):
        if list_s[i] == ' ' :
            answer += list_s[i]
            cnt = 0        
        elif cnt % 2 == 0 :
            answer += list_s[i].upper()
            cnt += 1
        elif cnt % 2 == 1 :
            answer += list_s[i].lower()
            cnt += 1
    return answer