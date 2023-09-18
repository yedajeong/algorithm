def time_cal(end, start):
    end_h = int(end.split(":")[0])
    end_m = int(end.split(":")[1])
    start_h = int(start.split(":")[0])
    start_m = int(start.split(":")[1])

    minute = 0

    if end_m < start_m:
        minute += 60 - (start_m - end_m)
        end_h -= 1
    else:
        minute += end_m - start_m
    minute += 60*(end_h - start_h)

    return minute

def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x: [int(x[0].split(":")[0]), int(x[0].split(":")[1]), int(x[1].split(":")[0]), int(x[1].split(":")[1])])

    book_num = []
    interval = time_cal(book_time[0][1], book_time[0][0])
    book_num.append([0, interval+10])  # 청소시간 +10

    for i in range(1, len(book_time)):
        end = book_time[i][1]
        start = book_time[i][0]
        origin = time_cal(start, book_time[0][0])
        interval = time_cal(end, start)

        book_num.append([origin, origin+interval+10])

    room = []
    for s, e in book_num:
        if not room:
            room.append([s, e])
        else:
            vacancy = False
            for i in range(len(room)):
                if room[i][1] <= s:
                    del room[i]
                    room.append([s, e])
                    vacancy = True
                    break
            if not vacancy:
                room.append([s, e])

    return len(room)

if __name__ == "__main__":
    book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
    print(solution(book_time))
