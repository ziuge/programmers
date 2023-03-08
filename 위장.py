import math

def solution(clothes):
    D = {}
    
    for items in clothes:
        if items[1] in D:
            D[items[1]] += 1
        else:
            D[items[1]] = 1
            
    new = [i + 1 for i in list(D.values())]
    return math.prod(new) - 1
