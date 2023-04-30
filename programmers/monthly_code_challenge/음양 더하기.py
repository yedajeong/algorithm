# 시즌2
# Lv. 1

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer

if __name__=="__main__":
    absolutes = [4, 7, 12]
    signs = [True, False, True]

    print(solution(absolutes, signs))