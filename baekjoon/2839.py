"""
https://www.acmicpc.net/problem/2839
"""

import sys

input = sys.stdin.readline

N = int(input())

if N % 5 == 0:
    print(N // 5)
elif N // 5 == 0:
    if N % 3 == 0:
        print(N // 3)
    else:
        print(-1)
else:
    count_of_five = N // 5
    count_of_three = 0
    while count_of_five >= 0:
        if (N - count_of_five * 5) % 3 == 0:
            count_of_three = (N - count_of_five * 5) // 3
            break
        count_of_five = count_of_five - 1

    if count_of_five * 5 + count_of_three * 3 == N:
        print(count_of_five + count_of_three)
    else:
        print(-1)
