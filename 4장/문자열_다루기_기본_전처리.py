import re

def solution(s):
    return len(s) in {4,6} and bool(re.match('^[0-9]*$', s))