def solution(phone_book):
    phone_book.sort()  # 전화번호를 정렬하면 접두어가 인접해 있을 것이다.
    
    for i in range(len(phone_book)-1):
        # 현재 전화번호와 그 다음 전화번호를 비교하여 접두어인지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False  # 접두어인 경우 False 반환
    
    return True
