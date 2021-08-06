d = [1, 3, 2, 5, 4]
budget = 9

# def solution(d, budget):
#     answer = 0
#
#     d.sort()
#     sum = 0
#     i = 0
#
#     for i in d:
#         sum += i
#         if sum > budget:
#             break
#         answer += 1
#
#     return answer
#
#
# print(solution(d, budget))



# 간단한 풀이! 대박
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)