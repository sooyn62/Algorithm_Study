def solution(x):
    answer = []
    answer.append(x)
    while x != 1:
        if x%2==0:
            x=x//2 #그냥 /하면 float으로 저장돼서 //권장

        else:
            x=x*3+1
        answer.append(x) #answer=[x]랑 동일
    
    return answer