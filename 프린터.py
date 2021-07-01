def solution(priorities, location):

    answer = 0
    Q = list(priorities)
    L = [i for i in range(len(Q))]

    while Q:
        x = Q.pop(0)
        l = L.pop(0)
        if not Q:
            answer += 1
            break
        elif x >= max(Q):
            answer += 1
            if l == location:
                break
        else:
            Q.append(x)
            L.append(l)

    return answer


# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer