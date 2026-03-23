def solution(n, wires):
    answer = []

    for k in range(len(wires)):
        W = wires.copy()
        W.remove(W[k])
        B, T, C, a, b = [], True, 0, 0, 0
        B.append(W[0][0])
        B.append(W[0][1])
        W.remove(W[0])
        while T:
            for k in range(len(W)):
                if W[k][0] in B or W[k][1] in B:
                    B.append(W[k][0])
                    B.append(W[k][1])
                    W.remove(W[k])
                    W.append([0,0])
                    C += 1
            if C == 0:
                T = False
            else:
                C = 0
        for z in range(len(W)):
            if W[z] != [0,0]:
                b += 1
        b += 1
        a = n - b 
        answer.append(abs(a-b))  
    
    return min(answer)