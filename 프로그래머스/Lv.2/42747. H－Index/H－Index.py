def solution(citations):
    citations.sort(reverse=True)  # 내림차순으로 정렬
    
    left, right = 0, len(citations) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if citations[mid] >= mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    
    return right + 1

