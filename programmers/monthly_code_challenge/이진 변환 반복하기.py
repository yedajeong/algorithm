# 시즌1
# Lv. 2

def solution(s):
    answer = [0, 0]

    while s!="1":
        answer[0] += 1
        answer[1] += s.count('0')

        s = s.replace('0', '')
        c = len(s)

        # 10진수 -> 2진수
        # 내장함수 아예 사용하지 x
        bin = []  # 뒤집어진 3진법
        while c:
            bin.append(str(c % 2))
            c //= 2

        bin.reverse()
        s = ''.join(bin)
    
    return answer

if __name__=="__main__":
    arr = "110010101001"

    print(solution(arr))
