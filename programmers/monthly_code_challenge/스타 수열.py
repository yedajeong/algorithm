# 시즌1
# Lv. 3

# count() 내장함수 제거하고 (O(N**2)만큼의 시간복잡도 -> 시간초과 실패)
# counting부분 직접 구현

# Max_time = 6988.18ms ms
# Memory = 91.2MB

def solution(a):
    answer = 0

    # 예외 처리
    if len(a) < 2:
        return 0
    
    cnt = [0]  * len(a)

    for item in a:
        cnt[item] += 1

    cnt_idx = []
    for i, num in enumerate(cnt):
        cnt_idx.append((i, num))

    cnt_idx.sort(key=lambda x: x[1])
    
    for item, num in cnt_idx:
        if answer >= num*2:  # num개로 만들 수 있는 최대 길이의 순열은 num*2개
            continue

        length = 0
        i = -1
        while i < len(a)-2:
            i += 1

            # 교집합 없는 경우 pass
            if a[i] != item and a[i+1] != item:
                continue
            
            # a[i] or a[i+1] 중 item과 같으나(교집합)
            # 둘이 같은 수인 경우 pass
            if a[i] == a[i+1]:
                continue

            length += 2
            i += 1

        answer = max(answer, length)
    
    return answer

if __name__=="__main__":
    # a = [5, 2, 3, 3, 5, 3]
    a = [0,3,3,0,7,2,0,2,2,0]

    print(solution(a))
