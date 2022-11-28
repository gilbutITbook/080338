import re
def solution(s):
    return re.sub('\d(?=\d{4})', '*', s)

