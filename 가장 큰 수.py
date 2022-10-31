# 가장 큰 수

'''
자릿수마다의 정렬을 준다 - 9, 8, 4 / 90, 86, 80, 40 / 900, 340, 330, 300
9로만 이루어진 수라면 앞에 붙인다

'''

def solution(numbers):
    answer = ''

    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    result = []
    for i in nums:
        result.append(int(''.join(i)))
    answer = max(result)

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))