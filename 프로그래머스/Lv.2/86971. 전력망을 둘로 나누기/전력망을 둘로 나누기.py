
def solution(n, wires):
    def dfs(node, visited):
        visited[node] = True
        count = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                count += dfs(neighbor, visited)
        return count

    min_difference = float('inf')
    
    for wire_to_remove in wires:
        graph = [[] for _ in range(n + 1)]
        for wire in wires:
            if wire != wire_to_remove:
                v1, v2 = wire
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        visited = [False] * (n + 1)
        components = []
        for node in range(1, n + 1):
            if not visited[node]:
                components.append(dfs(node, visited))
        
        # 각 전력망의 송전탑 개수 차이를 계산하여 최소 차이 업데이트
        difference = abs(components[0] - components[1])
        min_difference = min(min_difference, difference)
    
    return min_difference