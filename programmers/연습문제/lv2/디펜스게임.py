from queue import PriorityQueue

def solution(n, k, enemy):
    answer = -1

    if k >= len(enemy):
        return len(enemy)

    pq = PriorityQueue()

    for i in range(len(enemy)):
        if n >= enemy[i]:
            pq.put((-1*enemy[i], enemy[i])) # 내림차순
            n -= enemy[i]
        elif k > 0:
            k -= 1
            if not pq.empty():
                previous = pq.get()[1]
                if previous >= enemy[i]: # 제일 큰 enemy가 있었음 -> 무적권 쓰기
                    n = n + previous - enemy[i]
                    pq.put((-1*enemy[i], enemy[i]))
                else: # 무적권 못쓰거나 현재 enemy[i]랑 같거나 더 작을 때
                    pq.put((-1*previous, previous))
        else:
            answer = i-1 # 이전 라운드까지만 진행 가능했음
            break

    # 끝까지 다 순회한 경우 = 모든 라운드 수행 가능
    if i == len(enemy)-1 and answer == -1:
        return len(enemy)
    else:
        return answer+1 # 1-base로 변환

if __name__ == "__main__":
    n = 3
    k = 1
    enemy = [3, 4]
    print(solution(n, k, enemy))
