from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for per in list(permutations(dungeons,len(dungeons))):
        tmp = k 
        cnt = 0
        for p in per:
            if tmp >= p[0]:
                cnt +=1
                tmp -= p[1]
            else:
                break
        answer = max(cnt,answer)
    return answer