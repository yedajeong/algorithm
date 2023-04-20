# Lv. 2

def solution(line):
    answer = []
    cross = []
    
    # 1. 교점 구하기 (정수만)
    for i in range(len(line)-1):
        a1, b1, c1 = line[i]
        for j in range(i+1, len(line)):
            a2, b2, c2 = line[j]
            
            if a1*b2 == b1*a2:
                continue
            else:
                x = (b1*c2 - c1*b2) / (a1*b2 - b1*a2)
                y = (c1*a2 - a1*c2) / (a1*b2 - b1*a2)
                if x != float(int(x)) or y != float(int(y)):
                    continue
                else:
                    cross.append((x, y))
    
    xmin = sorted(cross, key=lambda x: x[0])[0][0]
    xmax = sorted(cross, key=lambda x: x[0])[-1][0]
    ymin = sorted(cross, key=lambda x: x[1])[0][1]
    ymax = sorted(cross, key=lambda x: x[1])[-1][1]
    
    # 2. 행, 열 개수만큼 바탕(.)찍기
    row = int(ymax - ymin)+1
    col = int(xmax - xmin)+1
    
    for i in range(row):
        answer.append("." * col)
        
    # 3. 모든 좌표에 xmin, ymin 만큼 빼서 원점(0, 0)으로 이동
    # y좌표는 col index와 반대
    for x, y in cross:
        x = int(x-xmin)
        y = int(row-(y-ymin)-1)
        tmp = list(answer[y])
        tmp[x] = "*"
        answer[y] = ''.join(tmp)
    
    return answer
