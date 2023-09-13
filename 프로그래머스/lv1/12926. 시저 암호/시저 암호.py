def solution(s, n):
    answer = ''
    # print(ord('A')) 65
    # print(ord('Z')) 90
    # print(ord('a')) 97
    # print(ord('z')) 122
    list_s = list(s)
    for i in range(len(list_s)) :
        code = ord(list_s[i])
        if list_s[i] == ' ' :
            answer += ' '
        if 65 <= code <= 90 :
            if code + n <= 90 :
                code += n
                answer += chr(code)
            elif code + n > 90 :
                code = 64 + (code+n -90)
                answer += chr(code)
        if 97 <= code <= 122 :
            if code + n <= 122 :    
                code += n
                answer += chr(code)
            elif code + n > 122 :
                code = 96 + (code+n -122)
                answer += chr(code)
                
    
    return answer