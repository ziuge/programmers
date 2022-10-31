# 전화번호 목록

def solution(phone_book):
    answer = True

    phone_book.sort()
    print(phone_book)
    p = {i:[] for i in range(1, 10)}
    print(p)
    for i in phone_book:
        print('i', i)
        print(i[0])
        p[i[0]].append(i)
    print(p)


    return answer

print(solution(["119", "97674223", "1195524421"]))