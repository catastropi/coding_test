from collections import defaultdict

def solution(array, commands):
    
    answer, t, k = [], defaultdict(int), 0
    
    for a, b, c in commands:
        t = sorted(array[a-1:b])
        k = t[c-1]
        answer.append(k)
    
    return answer