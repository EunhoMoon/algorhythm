"""
https://www.acmicpc.net/problem/2869
"""

A, B, V = map(int, input().split())
count = (V - B) // (A - B)
if (V - B) % (A - B) > 0:
    count += 1

print(count)
