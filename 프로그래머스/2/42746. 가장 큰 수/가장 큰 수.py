def solution(numbers):
    
    k, z  = sorted(list(map(lambda x: x*3, list(map(str, numbers)))), reverse = True), 0

    for n in range(len(k)):
        if k[n] == '000':
            k[n] = k[n][:(int(len(k[n])/3))]
            z += 1
        else:
            k[n] = k[n][:(int(len(k[n])/3))]
            
    if z == len(k):
        answer = '0'
    else:
        answer = ''.join(k)  
    return answer