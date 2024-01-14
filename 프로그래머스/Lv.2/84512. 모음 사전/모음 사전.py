def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    
    for i in range(len(word)):
        answer += vowels.index(word[i]) * (5 ** (5 - i) - 1) // (5 - 1)
    
    return answer + len(word)