"""
https://www.acmicpc.net/problem/2675
"""

N = int(input())

for _ in range(N):
    num, strs = input().split()
    arr = []
    for i in range(len(strs)):
        arr.extend([strs[i]] * int(num))

    print("".join(arr))
