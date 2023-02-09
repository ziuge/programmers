from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        for i in orders:
            combi = combinations(sorted(i), c) # 각 order에 대한 c개의 조합 생성
            temp += combi

        counter = Counter(temp) # 조합 중 가장 많은 경우를 나열

        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    
    return sorted(answer)
