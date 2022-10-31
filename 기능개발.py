# import sys
# import string
# from collections import deque
#
# pro = list(map(int, sys.stdin.readline().strip().strip(string.punctuation).split(',')))
# print(pro)
# sp = list(map(int, sys.stdin.readline().strip().strip(string.punctuation).split(',')))
# print(sp)
#
#
# def solution(progresses, speeds):
#     answer = []
#     Q = deque(progresses)
#     S = deque(speeds)
#     n = 1
#     cnt = 0
#
#     while True:
#         while Q[0] + (n * S[0]) < 100:
#             # print(Q[0], '+', n, '*', S[0], '=', Q[0] + (n * S[0]))
#             n += 1
#             # print()
#         while Q[0] + (n * S[0]) >= 100:
#             cnt += 1
#             # if len(Q) <= 1:
#             #     break
#             # else:
#             Q.popleft()
#             S.popleft()
#             if len(Q) == 0:
#                 break
#         answer.append(cnt)
#         # print(Q)
#         # print(S)
#         # print(answer)
#         # print()
#         cnt = 0
#         if len(Q) == 0:
#             break
#
#     return answer
#
#
# print(solution(pro, sp))
#
# '''
# [93, 30, 55]
# [1, 30, 5]
#
# [95, 90, 99, 99, 80, 99]
# [1, 1, 1, 1, 1, 1]
#
#
# '''
import sys
import string
from collections import deque

pro = list(map(int, sys.stdin.readline().strip()))
sp = list(map(int, sys.stdin.readline().strip()))


def solution(progresses, speeds):
    answer = []
    Q = deque(progresses)
    S = deque(speeds)
    n = 1
    cnt = 0

    while Q and S:
        while Q[0] + (n * S[0]) < 100:
            n += 1
        while Q[0] + (n * S[0]) >= 100:
            cnt += 1
            Q.popleft()
            S.popleft()
            if len(Q) == 0:
                break
        answer.append(cnt)
        cnt = 0


    return answer


print(solution(pro, sp))

#
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]