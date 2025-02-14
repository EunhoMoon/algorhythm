def solution(brown, yellow):
    answer = []

    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            y = i + 2
            x = yellow // i + 2
            if y * 2 + (x - 2) * 2 == brown:
                answer = [x, y]

    return answer
