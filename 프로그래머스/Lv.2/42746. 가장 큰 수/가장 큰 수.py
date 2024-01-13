def solution(numbers):
    # 숫자를 문자열로 변환하여 정렬하는 함수를 정의
    def custom_sort(x):
        return x * 3  # 각 숫자를 세 번 반복해서 비교

    # numbers를 문자열로 변환하고 custom_sort를 기준으로 정렬
    sorted_numbers = sorted(map(str, numbers), key=custom_sort, reverse=True)

    # 정렬된 숫자들을 이어붙여서 문자열로 반환
    answer = ''.join(sorted_numbers)
    
    # 만약 결과가 '0'으로만 이루어진 경우, '0'을 반환
    return str(int(answer))