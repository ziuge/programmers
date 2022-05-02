def solution(arr):
    answer = []
    if len(arr) < 2:
        answer.append(-1)
    else:
        arr.remove(min(arr))
        answer = arr
    return answer
