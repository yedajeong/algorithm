from collections import Counter

def solution(phone_book):
    answer = True
    
    phone_book.sort()

    for i in range(len(phone_book)-1):
        pre_len = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:pre_len]:
            return False

    return answer

phone_book = ["123","456","789"]
print(solution(phone_book))
