"""
https://www.acmicpc.net/problem/4880
"""

while True:
    a1, a2, a3 = map(int, input().split())

    if a1 == a2 == a3:
        break

    if a3 - a2 == a2 - a1:
        print(f"AP {a3 + a3 - a2}")
    else:
        print(f"GP {a3 * (a3 // a2)}")
