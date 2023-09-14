def time_cal(t1, t2):  # t1 < t2
    interval = 0

    t1_h = int(t1.split(':')[0])
    t1_m = int(t1.split(':')[1])
    t2_h = int(t2.split(':')[0])
    t2_m = int(t2.split(':')[1])

    if t2_m >= t1_m:
        interval += t2_m - t1_m
    else:
        interval += 60 - (t1_m - t2_m)
        t2_h -= 1

    interval += abs(t2_h - t1_h) * 60

    return interval


def solution(plans):
    answer = []
    stack = []  # (이름, 남은시간)
    time = []  # (이름, 시작시간, 끝시간)

    plans.sort(key = lambda x: [int(x[1].split(':')[0]), int(x[1].split(':')[1])])
    zero = plans[0][1]  # 원점 0
    time.append([plans[0][0], 0, int(plans[0][2])])

    for i in range(1, len(plans)):
        t = time_cal(zero, plans[i][1])
        time.append([plans[i][0], t, t + int(plans[i][2])])


    for i in range(0, len(time)-1):
        # 1) 다음 과제 시작 전 끝냄
        if time[i][2] <= time[i+1][1]: 
            answer.append(time[i][0])
            remain = time[i+1][1] - time[i][2]

            # 남은 시간 동안 중단한 과제
            while remain and stack:  
                next = stack.pop()
                # 중단했던 과제 끝냄
                if remain >= next[1]:  
                    remain -= next[1]
                    answer.append(next[0])
                # 다시 중단
                else: 
                    stack.append((next[0], next[1]-remain))
                    remain = 0
        
        # 2) 잠시 멈추고 다음 과제
        else:
            stack.append((time[i][0], time[i][2] - time[i+1][1]))

    # 시간 순서 마지막 남은 과제
    answer.append(time[-1][0])

    while stack:
        answer.append(stack.pop()[0])

    return answer


if __name__ == "__main__":
    plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]

    print(solution(plans))
