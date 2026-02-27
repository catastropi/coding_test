def solution(phone_book):
    phone_set = set(phone_book)
    
    for number in phone_book:
        prefix = ""
        for ch in number:
            prefix += ch
            # 자기 자신이 되기 전까지만 검사
            if prefix in phone_set and prefix != number:
                return False
    
    return True