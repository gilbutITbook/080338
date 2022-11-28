import re

def solution(s):
    '''전처리 방식'''
    return bool(re.match("^(\d{4}|\d{6})$", s))

    '''정규표현식 방식'''
    # return len(s) in {4,6} and bool(re.match('^[0-9]*$', s))
