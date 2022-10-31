from sqlite3 import IntegrityError


# ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1]

def solution(ingredient):
    answer = 0
    stack = ingredient[:3]

    for i in range(3, len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1] :
            answer += 1
            # stack = stack[:-4]
            for j in range(4):
                stack.pop()
    
    return answer
# 시간 초과.. 시간복잡도 n일텐데 for문 써서 그런가 으악!




print(solution(ingredient))
# 1231, stack