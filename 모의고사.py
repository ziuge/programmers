T = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    answer = []

    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
        # 1번
        if ((i % 5) + 1) == answers[i]:
            cnt[0] += 1

        # 2번
        if i % 2 == 0:
            if answers[i] == 2:
                cnt[1] += 1
        else:
            A = [1, 3, 4, 5]
            if A[(i // 2) % 4] == answers[i]:
                cnt[1] += 1

        # 3번
        B = [3, 1, 2, 4, 5]
        if B[(i // 2) % 5] == answers[i]:
            cnt[2] += 1

    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i + 1)

    return answer


print(solution(T))


# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result
