"""
https://www.acmicpc.net/problem/10996
"""

N = int(input())

for _ in range(N):
    first_line = []
    second_line = []
    for i in range(1, N + 1):
        if i % 2 == 1:
            first_line.append("*")
        else:
            second_line.append("*")

    print(" ".join(first_line))
    if second_line:
        print(" " + " ".join(second_line))
