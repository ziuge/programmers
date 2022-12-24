def solution(s):
    answer = 0
    
    for num in range(len(s)):
        if num > 0:
            new_s = s[num:] + s[0:num]
        else:
            new_s = s
        
        if new_s.count("(") == new_s.count(")") and new_s.count("[") == new_s.count("]") and new_s.count("{") == new_s.count("}"):

            # 올바른 괄호 문자열인지 확인
            stack = []
            for i in new_s:
                if i == "(" or i == "[" or i == "{":
                    stack.append(i)
                else:
                    if stack:
                        if i == ")" and stack[-1] == "(":
                            stack.pop()
                        elif i == "]" and stack[-1] == "[":
                            stack.pop()
                        elif i == "}" and stack[-1] == "{":
                            stack.pop()
            if len(stack) == 0:
                answer += 1
    
    return answer
