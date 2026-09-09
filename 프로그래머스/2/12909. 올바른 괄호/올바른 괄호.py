def solution(s):
    answer, lis, total = False, list(s), 0
    
    if len(s) == 1 or len(lis) % 2 != 0 or lis[0] == ')' or lis[len(lis)-1] =='(':
        return False
    else:
        for i in range(len(lis)):
            if total < 0:
                return False
            else:
                if lis[i] == '(':
                    total += 1
                else:
                    total -= 1
                
    if total == 0:
        return True
    else:
        return False
        