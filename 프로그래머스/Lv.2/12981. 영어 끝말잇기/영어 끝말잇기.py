def solution(n, words):
    answer = []
    stack = []

    for i in range(0, len(words)) :
        print(stack)
        if i == 0:
            stack.append(words[i])
        
        elif stack[-1][-1] == words[i][0] and words[i] not in stack:
            stack.append(words[i])
            
        
        elif stack[-1][-1] != words[i][0] or words[i] in stack:

            return [(i%n) +1, i//n + 1]
        
        
        if len(stack) == len(words) :
            return [0, 0]
        
    return answer