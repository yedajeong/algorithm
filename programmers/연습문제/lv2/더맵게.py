import heapq

def solution(scoville, K):
    answer = 0

    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        if first >= K:
            break

        heapq.heappush(heap, first + second*2)
        answer += 1

    if len(heap) == 1:
        if heap[0] < K :
            answer = -1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
