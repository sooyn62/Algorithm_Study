def solution(skill, skill_trees):
    count = 0
# 파이썬은 문자열을 리스트처럼 순회함

    for trees in skill_trees:
        temp=''
        for s in trees:
            if s in skill:
                temp += s
        if temp == skill[:len(temp)]:
            count += 1
            
    return count