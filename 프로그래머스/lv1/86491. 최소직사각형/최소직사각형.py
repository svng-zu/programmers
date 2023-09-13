def solution(sizes):
    answer = 0
    row = 0
    col = 0
    # a = sizes[0][0]
    # print(a)
    for i in range(len(sizes)) :
        sizes[i].sort()
        if sizes[i][0] > row :
            row = sizes[i][0]
        if sizes[i][1] > col :
            col = sizes[i][1]
    answer = row * col
    return answer