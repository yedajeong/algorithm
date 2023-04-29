# 시즌2
# Lv.2

# stack 이용 x -> 14번 test case인 s = "([{)}]" 에서 failed
# stack으로 풀도록 수정

def solution(s):
    answer = 0

    # x만큼 회전
    for x in range(len(s)):
        stack = []
        balance = True
        for i in range(len(s)):
            idx = (x+i)%len(s)
            item = s[idx]

            # open -> stack에 push
            if item in ["(", "[", "{"]:
                stack.append(item)

            # close -> stack에서 pop
            elif item in [")", "]", "}"]:
                # pop할 게 없는 경우 == close가 먼저 등장
                if not stack:
                    balance = False
                    break

                open = stack.pop()

                # 짝이 안 맞는 경우
                if item == ")" and open != "(":
                    balance = False
                    break
                elif item == "]" and open != "[":
                    balance = False
                    break
                elif item == "}" and open != "{":
                    balance = False
                    break

        if not stack and balance:
            answer += 1

            # elif item == ")":
            #     small -= 1
            # elif item == "[":
            #     mid += 1
            # elif item == "]":
            #     mid -= 1
            # elif item == "{":
            #     big += 1
            # elif item == "}":
            #     big -= 1
            
            # if small < 0 or mid < 0 or big < 0:
            #     break
        
        # if small == 0 and mid == 0 and big == 0:
        #     print(x)
        #     answer += 1
    
    return answer

if __name__=="__main__":
    # s = "[](){}"
    # s = "}]()[{"
    s = "([{)}]"

    print(solution(s))
