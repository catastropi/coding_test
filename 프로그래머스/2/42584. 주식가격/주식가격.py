def solution(prices):
    answer,num = [], 0
    
    for t in range(len(prices)-1):
        num = 0
        for y in range(t+1, len(prices)):
            num += 1
            if prices[t] > prices[y]:
                answer.append(num)
                break
        if len(answer) == t:
            answer.append(num)
    
    answer.append(0)
    return answer