from collections import defaultdict

def solution(genres, plays):
    
    hash, ar, answer, co = defaultdict(int), [], [], 0
    for k in range(len(genres)):
        hash[genres[k]] += plays[k]
    
    sorted_hash = dict(sorted(hash.items(), key=lambda x: x[1], reverse=True))
    
    for i in range(len(genres)):
        ar.append([genres[i], plays[i], i])
    
    k = sorted(ar, key=lambda x : (x[0], -x[1], x[2]))
    
    for p in sorted_hash.keys():
        for a, b, c in k:
            if p == a:
                if co == 2:
                    co = 0 
                    break
                else:
                    answer.append(c)
                    co += 1
        co = 0
            
                
    return answer