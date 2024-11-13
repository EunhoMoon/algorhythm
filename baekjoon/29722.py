"""
https://www.acmicpc.net/problem/29722
"""

Y, M, D = map(int, input().split("-"))
N = int(input())

M = M + (D + N) // 30
Y = Y + M // 12
M = M % 12
D = (D + N) % 30

if D == 0:
    D = 30
    M -= 1
if M == 0:
    M = 12
    Y -= 1

print(f"{Y}-{M if M >= 10 else '0' + str(M)}-{D if D >= 10 else '0' + str(D)}")
