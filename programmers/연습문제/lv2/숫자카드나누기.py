def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a % b)

def solution(arrayA, arrayB):
    answer = 0

    # 중복원소 제거
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))

    arrayA.sort()
    arrayB.sort()
    
    if len(arrayA) == 1:
        divA = arrayA[0]
    else:
        divA = gcd(arrayA[0], arrayA[1])
        for i in range(2, len(arrayA)):
            divA = gcd(divA, arrayA[i])
    
    if len(arrayB) == 1:
        divB = arrayB[0]
    else:
        divB = gcd(arrayB[0], arrayB[1])
        for i in range(2, len(arrayB)):
            divB = gcd(divB, arrayB[i])

    answerA = True  # divA가 answer의 후보
    answerB = True  # divB가 answer의 후보

    if divA == 1:
        answerA = False
    else:
        for a in arrayA:
            if a % divA != 0:
                answerA = False
                break

    if divB == 1:
        answerB = False
    else:
        for b in arrayB:
            if b % divB != 0:
                answerB = False
                break


    if answerA:  # div로 철수가 가진 카드들에 적힌 모든 숫자 나눌 수 o
        for b in arrayB:
            if b % divA == 0:
                answerA = False  # 영희 카드가 divA로 나눠짐
                break
        if answerA:
            answer = max(answer, divA)

    if answerB:  # divB로 영희가 가진 카드들에 적힌 모든 숫자 나눌 수 o
        for a in arrayA:
            if a % divB == 0:
                answerB = False  # 철수 카드가 divB로 나눠짐
                break
        if answerB:
            answer = max(answer, divB)

    return answer

if __name__ == "__main__":
    arrayA = [20, 40, 10]
    arrayB = [5, 17]

    print(solution(arrayA, arrayB))
