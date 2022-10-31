#K번째수

def solution(array, commands):
    answer = []

    for nums in commands:
        i, j, k = nums[0], nums[1], nums[2]
        new_list = sorted(array[i-1:j])
        answer.append(new_list[k-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))