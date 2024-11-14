"""
https://www.acmicpc.net/problem/25193
"""

N = int(input())
S = input().strip()
C = list(S).count("C")
NC = N - C + 1

print(C // NC + 1 if C % NC > 0 else C // NC)
