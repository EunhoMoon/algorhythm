"""
https://www.acmicpc.net/problem/1812
"""

N = int(input())
candys_sum = [int(input()) for _ in range(N)]

for first_candy in range(candys_sum[0] + 1):
    having_candy = [first_candy, candys_sum[0] - first_candy]
    is_valid = True

    for i in range(1, N):
        next_candy = candys_sum[i] - having_candy[i]

        if next_candy < 0:
            is_valid = False
            break

        having_candy.append(next_candy)

    if is_valid and having_candy[0] == having_candy[-1]:
        break

for candy in having_candy[:-1]:
    print(candy)
