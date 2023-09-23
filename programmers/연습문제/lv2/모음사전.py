from itertools import product

def solution(word):
    dictionary = []
    for i in range(1, 6):
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            w = ''.join(w)
            dictionary.append(w)

    dictionary.sort()
    return dictionary.index(word)+1


if __name__ == "__main__":
    word = "AAA"
    print(solution(word))
