def solution(number, k):
    answer = ''
    num_len = len(number) - k

    if int(number)==0:
        return "0"

    max_num = -1
    if k == len(number)-1:
        for num in number:
            if num == '9':
                return "9"
            elif max_num < int(num):
                max_num = int(num)
        return str(max_num)

    while k > 0 and num_len > 0:
        max_num = -1
        for i in range(k+1):
            if number[i] == '9':
                max_num = 9
                idx = i
                break
            elif max_num < int(number[i]):
                max_num = int(number[i])
                idx = i

        answer += str(max_num)
        k -= idx
        num_len -= 1
        number = number[idx+1:]

    if num_len > 0:
        answer += number

    return str(int(answer))


number = "0010"
print(solution(number, 3))
