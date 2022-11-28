def compress(s, length):
    words = [s[i:i+length] for i in range(0, len(s), length)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for pattern, compare in zip(words, words[1:] + ['']):
        if pattern == compare: cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(s):
    if len(s) == 1: return 1
    else: return min(compress(s, length) for length in list(range(1, len(s) // 2 + 1)))

