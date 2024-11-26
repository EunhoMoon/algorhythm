"""
https://www.acmicpc.net/problem/1316
"""

N = int(input())
count = 0

for _ in range(N):
    string = input().strip()
    arr = set([])
    prev = ""
    is_group = True

    for char in string:
        if char not in arr or char == prev:
            prev = char
            arr.add(char)
        else:
            is_group = False
            break

    if is_group:
        count += 1

print(count)
