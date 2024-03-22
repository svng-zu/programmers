def solution(n, results):
    # 그래프 초기화
    wins = {i: set() for i in range(1, n + 1)}
    loses = {i: set() for i in range(1, n + 1)}
    print(wins)
    for winner, loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)
    print(wins)
    # 모든 경기 결과에 대해 각 선수의 순위를 확인
    for i in range(1, n + 1):
        # i를 이긴 선수들은 i에게 진 선수들을 모두 이길 수 있음
        for loser in wins[i]:
            loses[loser].update(loses[i])
        
        # i에게 진 선수들은 i를 이긴 선수들에게 모두 질 수 있음
        for winner in loses[i]:
            wins[winner].update(wins[i])
    print("승리", wins)
    print("패배", loses)
    
    # 정확한 순위를 알 수 있는 선수의 수 계산
    count = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            count += 1

    return count
