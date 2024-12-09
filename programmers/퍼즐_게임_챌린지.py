def solution(diffs, times, limit):
    answer = 1
    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left + right) // 2
        if is_possible(diffs, times, limit, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def is_possible(diffs, times, limit, prev_diff):
    total = 0

    for i in range(len(diffs)):
        total += times[i]
        pesent_diff = diffs[i]

        if prev_diff < pesent_diff:
            total += (pesent_diff - prev_diff) * (times[i - 1] + times[i])
            if total > limit:
                return False

    return total <= limit
