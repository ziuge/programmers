def solution(s):
    answer = ""

    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    a = [str(j) for j in range(0, 10)]

    for i in range(len(s)):
        if s[i] in a:
            answer += s[i]
            # print(answer, "숫자")
        else:
            print('else')
            if s[i:i+3] in nums:
                answer += str(nums.index(s[i:i+3]))
                # print(answer)
            elif s[i:i+4] in nums:
                answer += str(nums.index(s[i:i+4]))
                # print(answer)
            elif s[i:i+5] in nums:
                answer += str(nums.index(s[i:i+5]))
                # print(answer)

    return int(answer)
