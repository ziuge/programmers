# s = "aabbaccc"
# s = "ababcdcdababcdcd"
s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"


def check(s, n): # n = 단위
    result = ''
    cnt = 1
    for i in range(0, len(s), n):
        if s[i:i+n] == s[i+n:i+n*2]:
            cnt += 1
            if i+n*2 == len(s):
                result = result + str(cnt) + s[i:i+n]
        else:
            if cnt == 1:
                result = result + s[i:i+n]
            elif cnt != 1 and i+n < len(s):
                result = result + str(cnt) + s[i:i+n]
                cnt = 1
    result = ''.join(i for i in result)
    return result


def solution(s):
    length = []
    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2+1):
        length.append(len(check(s, i)))

    return min(length)

print(solution(s))