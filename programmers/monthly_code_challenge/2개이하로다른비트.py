def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            num_bin = bin(num)
            num_bin = list('0' + str(num_bin)[2:])
            idx = 0

            for i in range(len(num_bin)-1, -1, -1):
                if num_bin[i]=='0':
                    idx = i
                    break

            num_bin[idx] = '1'
            num_bin[idx+1] = '0'

            answer.append(int(''.join(num_bin), 2))

    return answer

numbers = [2, 7, 11]
print(solution(numbers))
