def solution(array, commands):
    answer=[]
    
    for i in commands:
        select= array[i[0]-1:i[1]]
        select.sort()
        answer.append(select[i[2]-1])

    return answer