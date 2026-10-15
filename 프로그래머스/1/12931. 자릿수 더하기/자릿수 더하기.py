def solution(n):
    N = str(n)
    add_sum = 0
    for i in N:
        add_sum += int(str(i))
    
    return add_sum