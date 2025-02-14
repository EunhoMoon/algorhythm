"""
https://www.acmicpc.net/problem/3060
"""

N = int(input())

for _ in range(N):
    feedstuff = int(input())
    pigs = list(map(int, input().split()))
    days = 1

    while True:
        pigs_want = sum(pigs)

        if pigs_want > feedstuff:
            break

        days += 1
        new_pig = []

        for i in range(len(pigs)):
            left = i - 1
            right = i + 1 if i < 5 else 0
            opposite_side = i + 3 if i < 3 else i - 3

            new_pig.append(pigs[left] + pigs[i] + pigs[right] + pigs[opposite_side])

        pigs = new_pig

    print(days)
