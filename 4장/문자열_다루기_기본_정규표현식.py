import re

def solution(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))
