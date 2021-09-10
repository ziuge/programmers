# 거리두기 확인하기
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

dr = [-1, 1, 0, 0, -1, 1, -1, 1, -2, 2, 0, 0]
dc = [0, 0, -1, 1, -1, -1, 1, 1, 0, 0, -2, 2]


def solution(places):
    answer = []
    for i in range(5):
        check = 1
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    for l in range(12):
                        nj = j + dr[l]
                        nk = k + dc[l]
                        if 0<=nj<5 and 0<=nk<5 and places[i][nj][nk] == 'P':
                            if l < 4:
                                check = 0
                                break
                            elif 4 <= l < 8:
                                if places[i][nj][k] == places[i][j][nk] == 'X':
                                    continue
                                else:
                                    check = 0
                                    break
                            elif 8 <= l:
                                if places[i][(nj + j)//2][(nk + k)//2] == 'X':
                                    continue
                                else:
                                    check = 0
                                    break

        answer.append(check)
    return answer


print(solution(places))