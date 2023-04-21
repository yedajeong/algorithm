# 시즌 1
# Lv.1 

def solution(numbers):
    answer = []

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()  # .sort: 정렬된 리스트로 수정, return None
    # sorted(answer)  # sorted: 원본 유지, 정렬된 리스트를 return 

    return answer

if __name__=="__main__":
    numbers = [2,1,3,4,1]

    print(solution(numbers))
