def solution(citations):
    citations.sort()
    
    zz = 0
    
    for z in citations:
        if z == 0:
            zz += 1

    for i in range(len(citations)):
        if citations[i] >= len(citations) - (i):
            answer = len(citations) - (i)
            break
    
    if zz == len(citations):
        answer = 0

    return answer