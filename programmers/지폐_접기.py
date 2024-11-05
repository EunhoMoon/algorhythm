def solution(wallet, bill):
    answer = 0

    while True:
        if is_fit_wallet(wallet, bill):
            break
        answer += 1
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2

    return answer


def is_fit_wallet(wallet, bill):
    return max(bill[0], bill[1]) <= max(wallet[0], wallet[1]) and min(
        bill[0], bill[1]
    ) <= min(wallet[0], wallet[1])
