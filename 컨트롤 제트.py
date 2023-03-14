def solution(s):
    answer = 0
    s_list = list(s.split())
    
    for item in s_list:
        if item == "Z":
            answer -= temp
        else :
            answer += int(item)
            temp = int(item)
        
    return answer
