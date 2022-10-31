# s = "aabbaccc"
# s = "ababcdcdababcdcd"
s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"

# s를 n개 단위로 나누려고 할 때
def check(s, n): # n = 단위
    result = ''
    cnt = 1
    for i in range(0, len(s), n):
        if s[i:i+n] == s[i+n:i+n*2]: # n개 단위로 나눴을 때 같은 부분이 있으면 cnt+1
            cnt += 1
            if i+n*2 == len(s): # 만약 맨 끝이면 끝내고 result 뒤에 붙임
                result = result + str(cnt) + s[i:i+n]
        else: # 같은 부분이 없으면
            if cnt == 1:
                result = result + s[i:i+n] # result 뒤에 붙임
            elif cnt != 1 and i+n < len(s):
                result = result + str(cnt) + s[i:i+n] # result 뒤에 반복된 횟수와 함께 붙임
                cnt = 1
    result = ''.join(i for i in result)
    return result


def solution(s):
    length = []
    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2+1):
        length.append(len(check(s, i))) # length에 결괏값 하나씩 저장

    return min(length) # 가장 작은 값 return

print(solution(s))