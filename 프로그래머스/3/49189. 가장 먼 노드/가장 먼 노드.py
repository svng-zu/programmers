from collections import deque

def solution(n, edges):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문 여부를 저장할 리스트
    visited = [False] * (n + 1)
    # 최단 경로 저장을 위한 리스트
    distance = [0] * (n + 1)
    
    # BFS를 이용하여 최단 경로 구하기
    def bfs(start):
        queue = deque([(start, 0)])
        visited[start] = True
        
        while queue:
            node, dist = queue.popleft()
            distance[node] = dist
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
    
    # 1번 노드부터 BFS 수행
    bfs(1)
    
    # 가장 먼 노드까지의 거리 구하기
    max_distance = max(distance[1:])
    
    # 가장 먼 노드의 개수 세기
    answer = distance.count(max_distance)
    
    return answer