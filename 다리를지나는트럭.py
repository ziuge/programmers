def solution(bridge_length, weight, truck_weights):
    crossing = []
    t = 0

    while crossing or truck_weights:
        print('cro', crossing)
        print('tru', truck_weights)
        print('sum', list(crossing[i][0] for i in range(len(crossing))))
        if truck_weights and truck_weights[0] + sum(list(crossing[i][0] for i in range(len(crossing)))) <= weight:
            crossing.append([truck_weights[0], 0])
            del truck_weights[0]
        print('중간점검', crossing, truck_weights)

        for i in range(len(crossing)):
            crossing[i][1] += 1
        print('더하기 후', crossing)
        if crossing[0][1] == bridge_length:
            del crossing[0]
        t += 1
        print('t', t)

    answer = t + 1
    return answer

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))