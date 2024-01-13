def solution(s):

    tmp = 0
    
    if s[0:] == ')':
    
        return False

    for i in s :
        if i == '(' :
            tmp += 1
        if i == ')' :
            tmp -= 1
        if tmp < 0 :
            return False
    
    if tmp == 0 :
        return True
    else :
        return False
  