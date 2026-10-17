def solution(sizes):
    w_max = 0
    h_max = 0

    # 명함 하나에서 긴쪽, 하나에서 짧은 쪽 선택해서 회전해서 방향 통일될 수 있도록 함
    for size in sizes:
        w = max(size[0], size[1])
        h = min(size[1], size[0]) #가로, 세로 중 max로 하면 어떤 방향으로 주어져도 통과 가능함!
                    
        if w > w_max:
            w_max = w
        if h > h_max:
            h_max = h
                
    answer = w_max * h_max
    return answer