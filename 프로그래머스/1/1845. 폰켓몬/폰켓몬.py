def solution(nums):
    
    hash = {}
    
    for pocketmon in nums:
        if pocketmon in hash:
            hash[pocketmon] += 1
        else:
            hash[pocketmon] = 1
            
    answer = 0

    for pocket in hash.keys():
        answer += 1
        
    if answer > len(nums)/2:
        answer = len(nums)/2
        
    return answer