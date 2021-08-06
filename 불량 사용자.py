user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

from itertools import product

def check(x, y): # banned_id, user_id를 비교
    result = True
    for i in range(len(x)):
        if x[i] == '*':
            continue
        else:
            if x[i] == y[i]:
                continue
            else:
                result = False
                break

    return result


def solution(user_id, banned_id):
    answer = 0

    X = [] # banned_id에 해당할 수 있는 user_id를 모두 저장
    for i in banned_id: # banned_id에서 하나
        A = []
        for j in user_id: # user_id에서 하나 뽑기
            if len(i) == len(j) and check(i, j) == True: # 둘의 길이가 같고 check이 맞다면
                A.append(j) # A에 저장
        X.append(A)

    result = set() # 최종적으로 가능한 조합들
    pro = list(product(*X)) # product 함수 -> X에 있는 리스트에서 각각 하나씩 뽑아 조합 리스트를 만듦

    for i in pro:
        i = list(i)
        if len(set(i)) == len(banned_id): # 조합에서 중복을 제거(set())했을 때 길이가 같으면
            result.add(tuple(sorted(i))) # result에 add
    answer = len(result)

    return answer


print(solution(user_id, banned_id))
