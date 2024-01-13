def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = []  # 다리 위에 있는 트럭을 나타내는 리스트
    total_weight_on_bridge = 0  # 다리 위의 총 무게
    
    while truck_weights or on_bridge:
        answer += 1
        
        if on_bridge:
            # 다리 위에 있는 트럭의 이동
            for i in range(len(on_bridge)):
                on_bridge[i][1] += 1
            # 다리를 다 건넌 트럭 제거
            if on_bridge[0][1] > bridge_length:
                total_weight_on_bridge -= on_bridge.pop(0)[0]
        
        if truck_weights and total_weight_on_bridge + truck_weights[0] <= weight:
            # 다리에 새로운 트럭 추가
            truck = truck_weights.pop(0)
            on_bridge.append([truck, 1])
            total_weight_on_bridge += truck
        
    return answer