def solution(brown, yellow):
    answer = []
    import math

    x = yellow + brown
    for i in range(1, x // 2 + 1):
        if x % i == 0 and i <= math.sqrt(x):
            if (x // i - 2)*(i - 2) == yellow:
                answer.append(x//i)
                answer.append(i)
    
    return answer


print(solution(24, 24))
