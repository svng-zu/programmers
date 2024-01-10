def solution(s):
    a = list(s.split(' '))
    print(a)
    b = []
    for i in a :
        i = i.lower()
        if len(i) != 0:
            b.append(i[0].upper() + i[1:])
        else :
            b.append(i)
    
    return ' '.join(b)