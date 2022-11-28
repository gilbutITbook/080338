def solution(phone_book):
    headers = {}
    
    for phone_number in phone_book:
        headers[phone_number] = 1
    
    for phone_number in phone_book:
        header = ''
        for number in phone_number:
            header += number
            if header in headers and header != phone_number:
                return False
    return True
