from collections import deque


def solution(numbers, target):
    answer = 0
    dq = deque([(0, 0)])

    while dq:
        index, current_sum = dq.popleft()

        if index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            dq.append((index + 1, current_sum + numbers[index]))
            dq.append((index + 1, current_sum - numbers[index]))

    return answer
