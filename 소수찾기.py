# import itertools
#
# pool = ['1', '1', '0']
# X = []
# for i in range(len(pool)):
#     X.extend(list(map(''.join, itertools.permutations(pool, i+1))))
#
# X = list(set([int(i) for i in X]))
# X.sort()
#
# answer = []
#
# for i in X:
#     if i < 2:
#         continue
#     check = True
#     for j in range(2, i):
#         if i % j == 0:
#             check = False
#             break
#     if check:
#         answer.append(i)
#
#
# print(answer)

def solution(numbers):
    import itertools

    answer = 0

    N = list(numbers)
    X = []
    for i in range(len(N)):
        X.extend(list(map(''.join, itertools.permutations(N, i + 1))))

    X = list(set([int(i) for i in X]))
    X.sort()

    for i in X:
        if i < 2:
            continue
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            answer += 1

    return answer


# 다른 사람 풀이
#
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)