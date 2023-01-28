def solution(arr):
    answer = []

    if len(arr) == 1 or len(set(arr)) == 1:
        answer.append(-1)
    else :
        new = sorted(arr)
        temp = new[0]
        while temp in arr:
            arr.remove(temp)
        answer = arr

    return answer
