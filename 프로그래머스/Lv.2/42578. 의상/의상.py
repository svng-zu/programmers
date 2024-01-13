def solution(clothes):
    answer = 0
    mul = 1
    plus = 0
    hash = {}
    for i in clothes :

        if i[1] not in hash :
            hash[i[1]] = 1
        else :
            hash[i[1]] += 1
    len(hash.items())
    for k in hash.values() :
        mul *= k + 1
    return mul - 1