# 오픈채팅방

record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]


def solution(record):
    answer = []
    uid = {}
    result = []

    for i in record:
        t = i.split()
        if t[0] == 'Enter':
            uid[t[1]] = t[2]
            result.append([t[1], '님이 들어왔습니다.'])
        elif t[0] == 'Leave':
            result.append([t[1], '님이 나갔습니다.'])
        else:
            uid[t[1]] = t[2]

    for i in result:
        i[0] = uid.get(i[0])
        answer.append(''.join(j for j in i))

    return answer

print(solution(record))
