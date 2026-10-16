def solution(participant, completion):
    count={}
    
    #참가자 수 세기
    for name in participant:
        if name in count:
            count[name] += 1
        else:
            count[name]=1
    #완주자 수 빼기        
    for name in completion:
        count[name] -=1
    #남은 선수 찾기
    for name in count:
        if count[name]>0:
            return name
