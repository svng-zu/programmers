
def solution(n):
    answer = 0
    lenn = bin(n).count("1")
    nn = n+1
    print(lenn)
    while True :
        if bin(nn).count('1') == lenn :
            return nn
        nn +=1
            
