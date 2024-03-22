def solution(n, computers):
    def dfs(node):
        # 현재 노드 방문 처리
        visited[node] = True
        # 현재 노드와 연결된 모든 노드에 대해 재귀적으로 방문
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
    
    visited = [False] * n  # 방문 여부를 저장하는 배열
    count = 0  # 네트워크의 개수를 세는 변수
    
    # 모든 노드에 대해 방문하지 않은 경우 DFS 호출
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1  # 새로운 네트워크 시작
    
    return count