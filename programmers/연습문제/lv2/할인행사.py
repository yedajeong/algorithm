def solution(want, number, discount):
    answer = 0
    want_list = dict(zip(want, number))

    for i in range(0, len(discount)-10 + 1):
        this_week = discount[i:i+10]
        avail = True
        for item in want_list.keys():
            for _ in range(0, want_list[item]):
                if item in this_week:
                    this_week.remove(item)
                else:
                    avail = False
                    break
            if not avail: break
            
        if avail:
            answer += 1

    return answer


if __name__ == "__main__":
    want = ["banana", "apple", "rice", "pork", "pot"]
    number = [3, 2, 2, 2, 1]
    discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

    print(solution(want, number, discount))
