def solution(n):
    answer = 0
    k = ""

    while n > 0:
        n, m = divmod(n, 3)
        k += str(m)

    answer = int(k, 3)

    return answer
