"""
https://www.acmicpc.net/problem/17011
"""

N = int(input())

for _ in range(N):
    symbols = input().strip()
    present_symbol = symbols[0]
    count = 1
    result = []

    for i in range(1, len(symbols)):
        if symbols[i] == present_symbol:
            count += 1
        else:
            result.append(f"{count} {present_symbol}")
            present_symbol = symbols[i]
            count = 1

    result.append(f"{count} {present_symbol}")

    print(" ".join(result))
