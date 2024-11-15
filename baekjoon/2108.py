"""
https://www.acmicpc.net/problem/2108
"""

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
arr = []
sum_num = 0

for _ in range(N):
    num = int(input())
    arr.append(num)
    sum_num += num

arr.sort()


def round_impl(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    elif num - int(num) < -0.5:
        return int(num) - 1
    else:
        return int(num)


mod_dict = Counter(arr)
max_count = max(mod_dict.values())
mod_values = sorted([num for num, count in mod_dict.items() if count == max_count])


print(round_impl(sum_num / N))
print(arr[N // 2])
print(mod_values[1] if len(mod_values) > 1 else mod_values[0])
print(arr[-1] - arr[0])
