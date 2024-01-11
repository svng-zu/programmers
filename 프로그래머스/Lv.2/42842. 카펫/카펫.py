def solution(brown, yellow):

    total = brown + yellow
    
    width = 3
    height = 1
    
    while True :
        height = total // width
        remainder = total % width
        
        if remainder == 0 and width >= height and yellow == (width-2) * (height -2) :
            return [width, height]
        
        width +=1
    