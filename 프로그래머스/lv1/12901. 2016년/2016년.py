def solution(a, b):
    answer = ''
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = 0
    if a == 1 :
        day = b % 7
        answer = week[day-1]
    else :
        for i in range(a-1) :
            day += days[i]
        day = (day + b)%7
        
        answer = week[day-1]
          
    return answer