# 병합 정렬 실전문제
# 1517
# 플래티넘

'''
<Key Idea>
N: 50만개의 데이터 -> O(n^2)의 시간복잡도 알고리즘으로는 풀 수 없음
시간제한: 1초 (파이썬 _ 1초에 2천만번~1억번)
버블정렬 시간복잡도: O(n^2)
-> 버블정렬 쓰면 안된다는 소리
-> 따라서 O(nlogn)인 병합정렬을 사용한다!
-> "병합정렬 과정 내에 버블정렬의 swap이 포함되어 있다" 
'''

import sys
input = sys.stdin.readline


# 재귀함수로 구현
def merge_sort(start, end):
    global result  # 정답값 저장

    # 더이상 자를 수 없을 때 (재귀 멈춤)
    if end - start < 1:
        return

    mid = int(start + (end-start)/2)
    merge_sort(start, mid)
    merge_sort(mid+1, end)

    for i in range(start, end+1):
        tmp[i] = A[i]

    # 나눈 부분집합 각각의 가장 첫번째 원소
    k = start  # 정렬 하면서 배열 A의 어느 위치에 들어가야 하는지 나타낼 인덱스
    idx1 = start
    idx2 = mid + 1
    while idx1 <= mid and idx2 <= end:
        if tmp[idx1] > tmp[idx2]:
            A[k] = tmp[idx2]
            result += idx2 - k  # idx2가 놓여야 할 배열 A상에서의 위치까지 거리만큼 swap 카운트
            idx2 += 1
        else:
            A[k] = tmp[idx1]
            idx1 += 1

        k += 1

    # 두 부분집합 중 남아있는 애들이 있는 경우
    while idx1 <= mid:
        A[k] = tmp[idx1]
        k += 1
        idx1 += 1
    
    while idx2 <= end:
        A[k] = tmp[idx2]
        k += 1
        idx2 += 1


result = 0
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)  # 1 based indexing을 위함 (0번째 인덱스에 0 넣어줌, 1부터 인덱싱 가능)
tmp = [0] * (N+1)  # A로부터 정렬 완료된 배열


merge_sort(1, N)
print(result)

