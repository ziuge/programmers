def solution(arr):
    import math
    answer = arr[0]

    for i in range(1, len(arr)):
        g = math.gcd(answer, arr[i])
        answer = (answer * arr[i]) // g

    return answer
